from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.invoice_item import (
    InvoiceItemCreate,
    InvoiceItemUpdate,
    InvoiceItemResponse,
)
from app.services.invoice_item_service import InvoiceItemService

router = APIRouter(
    prefix="/invoices/{invoice_id}/items",
    tags=["Invoice Items"],
)


@router.get("/", response_model=list[InvoiceItemResponse])
def list_items(
    invoice_id: int,
    db: Session = Depends(get_db),
):
    return InvoiceItemService.list(db, invoice_id)


@router.post(
    "/",
    response_model=InvoiceItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_item(
    invoice_id: int,
    item: InvoiceItemCreate,
    db: Session = Depends(get_db),
):
    data = item.model_dump()
    data["invoice_id"] = invoice_id
    return InvoiceItemService.create(db, data)


@router.put("/{item_id}", response_model=InvoiceItemResponse)
def update_item(
    invoice_id: int,
    item_id: int,
    item: InvoiceItemUpdate,
    db: Session = Depends(get_db),
):
    try:
        return InvoiceItemService.update(
            db,
            item_id,
            item.model_dump(exclude_unset=True),
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


@router.delete("/{item_id}")
def delete_item(
    invoice_id: int,
    item_id: int,
    db: Session = Depends(get_db),
):
    try:
        InvoiceItemService.delete(db, item_id)
        return {"message": "Invoice item deleted successfully"}
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )
