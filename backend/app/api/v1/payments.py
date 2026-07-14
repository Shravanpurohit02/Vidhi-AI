from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.payment import (
    PaymentCreate,
    PaymentResponse,
)
from app.services.payment_service import PaymentService

router = APIRouter(
    prefix="/payments",
    tags=["Payments"],
)


@router.post("/", response_model=PaymentResponse, status_code=201)
def create_payment(
    payment: PaymentCreate,
    db: Session = Depends(get_db),
):
    try:
        return PaymentService.create(
            db,
            payment.model_dump(),
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@router.get("/", response_model=list[PaymentResponse])
def list_payments(
    db: Session = Depends(get_db),
):
    return PaymentService.list(db)


@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment(
    payment_id: int,
    db: Session = Depends(get_db),
):
    try:
        return PaymentService.get(
            db,
            payment_id,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@router.get("/invoice/{invoice_id}", response_model=list[PaymentResponse])
def list_invoice_payments(
    invoice_id: int,
    db: Session = Depends(get_db),
):
    return PaymentService.list_by_invoice(
        db,
        invoice_id,
    )


@router.delete("/{payment_id}")
def delete_payment(
    payment_id: int,
    db: Session = Depends(get_db),
):
    try:
        PaymentService.delete(
            db,
            payment_id,
        )
        return {"message": "Payment deleted successfully"}
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )
