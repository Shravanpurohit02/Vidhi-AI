from sqlalchemy.orm import Session

from app.models.client_ledger import ClientLedger


class ClientLedgerRepository:

    @staticmethod
    def create(db: Session, data: dict):
        entry = ClientLedger(**data)
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry

    @staticmethod
    def list_by_client(db: Session, client_id: int):
        return (
            db.query(ClientLedger)
            .filter(ClientLedger.client_id == client_id)
            .order_by(ClientLedger.entry_date.asc())
            .all()
        )

    @staticmethod
    def list_by_invoice(db: Session, invoice_id: int):
        return (
            db.query(ClientLedger)
            .filter(ClientLedger.invoice_id == invoice_id)
            .order_by(ClientLedger.entry_date.asc())
            .all()
        )
