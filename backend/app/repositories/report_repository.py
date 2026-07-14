from datetime import datetime

from sqlalchemy.orm import Session

from app.models.invoice import Invoice


class ReportRepository:

    @staticmethod
    def outstanding_invoices(db: Session):
        return (
            db.query(Invoice)
            .filter(Invoice.balance_due > 0)
            .order_by(
                Invoice.due_date.asc(),
                Invoice.invoice_number.asc(),
            )
            .all()
        )

    @staticmethod
    def paid_invoices(db: Session):
        return (
            db.query(Invoice)
            .filter(Invoice.balance_due <= 0)
            .order_by(
                Invoice.issue_date.desc(),
            )
            .all()
        )

    @staticmethod
    def overdue_invoices(db: Session):
        return (
            db.query(Invoice)
            .filter(
                Invoice.balance_due > 0,
                Invoice.due_date < datetime.utcnow(),
            )
            .order_by(
                Invoice.due_date.asc(),
            )
            .all()
        )
