from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.client_ledger_repository import ClientLedgerRepository
from app.schemas.client_ledger import ClientLedgerResponse

router = APIRouter(
    prefix="/ledger",
    tags=["Client Ledger"],
)


@router.get(
    "/client/{client_id}",
    response_model=list[ClientLedgerResponse],
)
def get_client_ledger(
    client_id: int,
    db: Session = Depends(get_db),
):
    return ClientLedgerRepository.list_by_client(
        db,
        client_id,
    )


@router.get(
    "/invoice/{invoice_id}",
    response_model=list[ClientLedgerResponse],
)
def get_invoice_ledger(
    invoice_id: int,
    db: Session = Depends(get_db),
):
    return ClientLedgerRepository.list_by_invoice(
        db,
        invoice_id,
    )
