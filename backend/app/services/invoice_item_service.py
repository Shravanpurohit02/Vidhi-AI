from sqlalchemy.orm import Session

from app.repositories.invoice_item_repository import InvoiceItemRepository
from app.services.invoice_calculation_service import InvoiceCalculationService


class InvoiceItemService:

    @staticmethod
    def create(db: Session, data: dict):
        item = InvoiceItemRepository.create(db, data)
        InvoiceCalculationService.recalculate(db, item.invoice_id)
        return item

    @staticmethod
    def list(db: Session, invoice_id: int):
        return InvoiceItemRepository.list_by_invoice(
            db,
            invoice_id,
        )

    @staticmethod
    def update(db: Session, item_id: int, data: dict):
        item = InvoiceItemRepository.get(db, item_id)

        if item is None:
            raise ValueError("Invoice item not found")

        for key, value in data.items():
            setattr(item, key, value)

        item = InvoiceItemRepository.update(db, item)
        InvoiceCalculationService.recalculate(db, item.invoice_id)
        return item

    @staticmethod
    def delete(db: Session, item_id: int):
        item = InvoiceItemRepository.get(db, item_id)

        if item is None:
            raise ValueError("Invoice item not found")

        invoice_id = item.invoice_id
        InvoiceItemRepository.delete(db, item)
        InvoiceCalculationService.recalculate(db, invoice_id)
