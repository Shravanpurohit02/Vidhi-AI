from sqlalchemy.orm import Session

from app.repositories.document_repository import DocumentRepository
from app.utils.file_storage import FileStorage


class DocumentService:

    @staticmethod
    def create_document(db: Session, data: dict):
        return DocumentRepository.create(db, data)

    @staticmethod
    def list_documents(db: Session):
        return DocumentRepository.list_all(db)

    @staticmethod
    def get_document(db: Session, document_id: int):
        document = DocumentRepository.get_by_id(db, document_id)

        if document is None:
            raise ValueError("Document not found")

        return document

    @staticmethod
    def search_documents(db: Session, query: str):
        return DocumentRepository.search(db, query)

    @staticmethod
    def list_case_documents(db: Session, case_id: int):
        return DocumentRepository.list_by_case(db, case_id)

    @staticmethod
    def delete_document(db: Session, document_id: int):
        document = DocumentRepository.get_by_id(db, document_id)

        if document is None:
            raise ValueError("Document not found")

        FileStorage.delete(document.file_path)
        DocumentRepository.delete(db, document)
