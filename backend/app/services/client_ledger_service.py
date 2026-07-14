from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.client_ledger import ClientLedger
from app.repositories.client_ledger_repository import ClientLedgerRepository


class ClientLedgerService:

    @staticmethod
    def add_entry(db: Session, data: dict):
        last = (
            db.query(ClientLedger)
            .filter(ClientLedger.client_id == data["client_id"])
            .order_by(ClientLedger.id.desc())
            .first()
        )

        previous_balance = Decimal(str(last.balance if last else 0))

        debit = Decimal(str(data.get("debit", 0)))
        credit = Decimal(str(data.get("credit", 0)))

        data["balance"] = previous_balance + debit - credit

        return ClientLedgerRepository.create(db, data)

    @staticmethod
    def list_by_client(db: Session, client_id: int):
        return ClientLedgerRepository.list_by_client(
            db,
            client_id,
        )
