from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.report import InvoiceReportResponse
from app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get(
    "/outstanding",
    response_model=List[InvoiceReportResponse],
)
def outstanding_invoices(
    db: Session = Depends(get_db),
):
    return ReportService.outstanding_invoices(db)


@router.get(
    "/paid",
    response_model=List[InvoiceReportResponse],
)
def paid_invoices(
    db: Session = Depends(get_db),
):
    return ReportService.paid_invoices(db)


@router.get(
    "/overdue",
    response_model=List[InvoiceReportResponse],
)
def overdue_invoices(
    db: Session = Depends(get_db),
):
    return ReportService.overdue_invoices(db)
