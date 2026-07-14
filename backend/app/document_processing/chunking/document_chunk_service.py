from __future__ import annotations

from sqlalchemy.orm import Session

from app.ai.chunking.chunker import TextChunker
from app.database.database import SessionLocal
from app.models.document_chunk import DocumentChunk


class DocumentChunkService:

    def __init__(self):
        self.chunker = TextChunker()

    def create_chunks(
        self,
        document_id: int,
        text: str,
    ) -> list[DocumentChunk]:

        chunks = self.chunker.chunk(text)

        db: Session = SessionLocal()

        try:

            records = []

            for index, chunk in enumerate(chunks):

                record = DocumentChunk(
                    document_id=document_id,
                    chunk_index=index,
                    text=chunk,
                    token_count=len(chunk.split()),
                    metadata_json={},
                )

                db.add(record)
                records.append(record)

            db.commit()

            for record in records:
                db.refresh(record)

            return records

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()
