from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService
from app.utils.file_storage import FileStorage

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
