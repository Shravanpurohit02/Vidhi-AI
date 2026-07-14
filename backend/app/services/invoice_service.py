from sqlalchemy.orm import Session

from app.repositories.invoice_repository import InvoiceRepository
from app.services.invoice_number_service import InvoiceNumberService
from app.services.client_ledger_service import ClientLedgerService


class InvoiceService:

    @staticmethod
    def create(db: Session, data: dict):

        if not data.get("invoice_number"):
            data["invoice_number"] = InvoiceNumberService.generate(db)

        if InvoiceRepository.exists(db, data["invoice_number"]):
            raise ValueError("Invoice number already exists")

        if not data.get("invoice_number"):
            data["invoice_number"] = InvoiceNumberService.generate(db)

        invoice = InvoiceRepository.create(db, data)

        ClientLedgerService.add_entry(
            db,
            {
                "client_id": invoice.client_id,
                "invoice_id": invoice.id,
                "entry_type": "Invoice",
                "debit": invoice.total_amount,
                "credit": 0,
                "remarks": f"Invoice {invoice.invoice_number}",
            },
        )

        return invoice

    @staticmethod
    def list(db: Session):
        return InvoiceRepository.list(db)

    @staticmethod
    def get(db: Session, invoice_id: int):
        invoice = InvoiceRepository.get(db, invoice_id)

        if invoice is None:
            raise ValueError("Invoice not found")

        return invoice

    @staticmethod
    def update(db: Session, invoice_id: int, data: dict):
        invoice = InvoiceService.get(db, invoice_id)
        return InvoiceRepository.update(db, invoice, data)

    @staticmethod
    def delete(db: Session, invoice_id: int):
        invoice = InvoiceService.get(db, invoice_id)
        InvoiceRepository.delete(db, invoice)
