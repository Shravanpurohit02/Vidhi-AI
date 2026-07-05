from fastapi import APIRouter, Body, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/")
def list_documents(db: Session = Depends(get_db)):
    return DocumentService.list_documents(db)


@router.get("/search", response_model=list[DocumentResponse])
def search_documents(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    return DocumentService.search_documents(db, q)


@router.get("/case/{case_id}", response_model=list[DocumentResponse])
def documents_for_case(
    case_id: int,
    db: Session = Depends(get_db),
):
    return DocumentService.list_case_documents(db, case_id)


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    try:
        DocumentService.delete_document(db, document_id)
        return {"message": "Document deleted successfully"}
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.post("/process/{document_id}")
def process_document(
    document_id: int,
    text: str = Body(..., embed=True),
    db: Session = Depends(get_db),
):
    try:
        return DocumentService.process_document(
            db,
            document_id,
            text,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )
