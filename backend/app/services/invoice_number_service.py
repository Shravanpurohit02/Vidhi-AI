from datetime import datetime

from sqlalchemy.orm import Session

from app.models.invoice import Invoice


class InvoiceNumberService:

    PREFIX = "INV"

    @classmethod
    def generate(cls, db: Session) -> str:
        year = datetime.utcnow().year

        latest = db.query(Invoice).order_by(Invoice.id.desc()).first()

        if latest is None:
            number = 1
        else:
            number = latest.id + 1

        return f"{cls.PREFIX}-{year}-{number:06d}"
