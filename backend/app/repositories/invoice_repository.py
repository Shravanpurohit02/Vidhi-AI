from sqlalchemy.orm import Session

from app.models.invoice import Invoice


class InvoiceRepository:

    @staticmethod
    def create(db: Session, data: dict):
        obj = Invoice(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def list(db: Session):
        return db.query(Invoice).order_by(Invoice.id.desc()).all()

    @staticmethod
    def get(db: Session, invoice_id: int):
        return db.query(Invoice).filter(Invoice.id == invoice_id).first()

    @staticmethod
    def exists(db: Session, invoice_number: str):
        return (
            db.query(Invoice).filter(Invoice.invoice_number == invoice_number).first()
        )

    @staticmethod
    def update(db: Session, invoice, data: dict):
        for key, value in data.items():
            if value is not None:
                setattr(invoice, key, value)

        db.commit()
        db.refresh(invoice)
        return invoice

    @staticmethod
    def delete(db: Session, invoice):
        db.delete(invoice)
        db.commit()
