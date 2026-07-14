from sqlalchemy.orm import Session

from app.models.invoice_item import InvoiceItem


class InvoiceItemRepository:

    @staticmethod
    def create(db: Session, data: dict):
        item = InvoiceItem(**data)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def list_by_invoice(db: Session, invoice_id: int):
        return db.query(InvoiceItem).filter(InvoiceItem.invoice_id == invoice_id).all()

    @staticmethod
    def get(db: Session, item_id: int):
        return db.query(InvoiceItem).filter(InvoiceItem.id == item_id).first()

    @staticmethod
    def update(db: Session, item: InvoiceItem):
        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def delete(db: Session, item: InvoiceItem):
        db.delete(item)
        db.commit()
