from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.invoice_repository import InvoiceRepository
from app.services.pdf_service import PDFService

router = APIRouter(
    prefix="/invoices",
    tags=["Invoice PDF"],
)


@router.get("/{invoice_id}/pdf")
def download_invoice_pdf(
    invoice_id: int,
    db: Session = Depends(get_db),
):
    invoice = InvoiceRepository.get(db, invoice_id)

    if invoice is None:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found",
        )

    pdf = PDFService.generate_invoice(db, invoice)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="{invoice.invoice_number}.pdf"'
        },
    )
