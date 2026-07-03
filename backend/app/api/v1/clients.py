from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.client import ClientCreate, ClientResponse
from app.services.client_service import ClientService

router = APIRouter(
    prefix="/clients",
    tags=["Clients"],
)


@router.post("/", response_model=ClientResponse)
def create_client(
    client: ClientCreate,
    db: Session = Depends(get_db),
):
    return ClientService.create(db, client.model_dump())


@router.get("/", response_model=list[ClientResponse])
def list_clients(
    db: Session = Depends(get_db),
):
    return ClientService.list(db)
