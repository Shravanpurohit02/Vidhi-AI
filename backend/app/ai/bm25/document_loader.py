from __future__ import annotations

from app.database.database import SessionLocal
from app.models.document_chunk import DocumentChunk


class DocumentLoader:

    @staticmethod
    def load():

        db=SessionLocal()

        try:
            return [
                (x.id,x.text)
                for x in db.query(DocumentChunk).all()
            ]
        finally:
            db.close()
