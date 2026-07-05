from sqlalchemy.orm import Session

from app.document_processing import DocumentProcessingService
from app.tasks.document_tasks import DocumentTasks
from app.repositories.document_repository import DocumentRepository
from app.utils.file_storage import FileStorage
from app.core.logging import get_logger

logger = get_logger()


class DocumentService:

    processor = DocumentProcessingService()

    @staticmethod
    def create_document(db: Session, data: dict):
        document = DocumentRepository.create(db, data)

        try:
            DocumentTasks.process_uploaded_document(
                document,
            )
        except Exception:
            logger.exception("Document post-processing failed")

        return document

    @staticmethod
    def list_documents(db: Session):
        return DocumentRepository.list(db)

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

    @classmethod
    def process_document(
        cls,
        db: Session,
        document_id: int,
        text: str,
    ):
        document = cls.get_document(
            db,
            document_id,
        )

        return cls.processor.process(
            document.id,
            text,
        )

    @staticmethod
    def delete_document(db: Session, document_id: int):
        document = DocumentRepository.get_by_id(
            db,
            document_id,
        )

        if document is None:
            raise ValueError("Document not found")

        FileStorage.delete(document.file_path)
        DocumentRepository.delete(db, document)
