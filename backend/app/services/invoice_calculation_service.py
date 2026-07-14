from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.models.invoice_item import InvoiceItem


class InvoiceCalculationService:

    @classmethod
    def recalculate(cls, db: Session, invoice_id: int):
        invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()

        if invoice is None:
            raise ValueError("Invoice not found")

        items = db.query(InvoiceItem).filter(InvoiceItem.invoice_id == invoice_id).all()

        subtotal = sum(
            (
                Decimal(str(item.quantity)) * Decimal(str(item.unit_price))
                for item in items
            ),
            Decimal("0.00"),
        )

        discount = Decimal(str(invoice.discount_amount or 0))

        total = subtotal - discount

        if total < Decimal("0.00"):
            total = Decimal("0.00")

        invoice.subtotal = float(subtotal.quantize(Decimal("0.01")))
        invoice.tax_amount = 0.0
        invoice.total_amount = float(total.quantize(Decimal("0.01")))

        db.commit()
        db.refresh(invoice)

        return invoice
