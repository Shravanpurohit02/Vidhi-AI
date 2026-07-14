from sqlalchemy.orm import Session

from app.models.payment import Payment


class PaymentRepository:

    @staticmethod
    def create(db: Session, data: dict):
        payment = Payment(**data)
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment

    @staticmethod
    def get(db: Session, payment_id: int):
        return db.query(Payment).filter(Payment.id == payment_id).first()

    @staticmethod
    def list(db: Session):
        return db.query(Payment).order_by(Payment.payment_date.desc()).all()

    @staticmethod
    def list_by_invoice(db: Session, invoice_id: int):
        return (
            db.query(Payment)
            .filter(Payment.invoice_id == invoice_id)
            .order_by(Payment.payment_date.desc())
            .all()
        )

    @staticmethod
    def update(db: Session, payment: Payment):
        db.commit()
        db.refresh(payment)
        return payment

    @staticmethod
    def delete(db: Session, payment: Payment):
        db.delete(payment)
        db.commit()
