from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    @staticmethod
    def create(db: Session, data: dict):
        document = Document(**data)
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def get_by_id(db: Session, document_id: int):
        return db.query(Document).filter(Document.id == document_id).first()

    @staticmethod
    def list(db: Session):
        return db.query(Document).order_by(Document.id.desc()).all()

    @staticmethod
    def list_by_case(db: Session, case_id: int):
        return (
            db.query(Document)
            .filter(Document.case_id == case_id)
            .order_by(Document.id.desc())
            .all()
        )

    @staticmethod
    def search(db: Session, query: str):
        return (
            db.query(Document)
            .filter(
                or_(
                    Document.title.ilike(f"%{query}%"),
                    Document.filename.ilike(f"%{query}%"),
                )
            )
            .all()
        )

    @staticmethod
    def delete(db: Session, document):
        db.delete(document)
        db.commit()
