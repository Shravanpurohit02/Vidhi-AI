from decimal import Decimal

from sqlalchemy.orm import Session

from app.constants.invoice_status import InvoiceStatus
from app.repositories.invoice_repository import InvoiceRepository
from app.repositories.payment_repository import PaymentRepository
from app.services.client_ledger_service import ClientLedgerService


class PaymentService:

    @staticmethod
    def create(db: Session, data: dict):
        invoice = InvoiceRepository.get(db, data["invoice_id"])

        if invoice is None:
            raise ValueError("Invoice not found")

        payment_amount = Decimal(str(data["amount"]))
        amount_paid = Decimal(str(invoice.amount_paid or 0))
        total_amount = Decimal(str(invoice.total_amount or 0))

        if payment_amount <= Decimal("0.00"):
            raise ValueError("Payment amount must be greater than zero")

        outstanding = total_amount - amount_paid

        if payment_amount > outstanding:
            raise ValueError("Payment exceeds outstanding balance")

        payment = PaymentRepository.create(db, data)

        invoice.amount_paid = amount_paid + payment_amount
        invoice.balance_due = total_amount - invoice.amount_paid

        if invoice.amount_paid <= Decimal("0.00"):
            invoice.status = InvoiceStatus.ISSUED
        elif invoice.balance_due > Decimal("0.00"):
            invoice.status = InvoiceStatus.PARTIALLY_PAID
        else:
            invoice.status = InvoiceStatus.PAID

        db.add(invoice)
        db.commit()
        db.refresh(invoice)

        ClientLedgerService.add_entry(
            db,
            {
                "client_id": invoice.client_id,
                "invoice_id": invoice.id,
                "payment_id": payment.id,
                "entry_type": "Payment",
                "debit": 0,
                "credit": payment.amount,
                "remarks": f"Payment received ({payment.payment_method})",
            },
        )

        return payment

    @staticmethod
    def list(db: Session):
        return PaymentRepository.list(db)

    @staticmethod
    def list_by_invoice(db: Session, invoice_id: int):
        return PaymentRepository.list_by_invoice(db, invoice_id)

    @staticmethod
    def get(db: Session, payment_id: int):
        payment = PaymentRepository.get(db, payment_id)

        if payment is None:
            raise ValueError("Payment not found")

        return payment

    @staticmethod
    def delete(db: Session, payment_id: int):
        payment = PaymentService.get(db, payment_id)
        PaymentRepository.delete(db, payment)
