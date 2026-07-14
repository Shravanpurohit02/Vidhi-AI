from __future__ import annotations

from sqlalchemy.orm import Session

from app.models.document_chunk import DocumentChunk


class DocumentChunkRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        *,
        document_id: int,
        chunk_index: int,
        text: str,
        token_count: int = 0,
        page_number: int | None = None,
        section: str | None = None,
        metadata_json: dict | None = None,
    ) -> DocumentChunk:

        chunk = DocumentChunk(
            document_id=document_id,
            chunk_index=chunk_index,
            text=text,
            token_count=token_count,
            page_number=page_number,
            section=section,
            metadata_json=metadata_json or {},
        )

        self.db.add(chunk)
        self.db.commit()
        self.db.refresh(chunk)

        return chunk

    def list_by_document(
        self,
        document_id: int,
    ) -> list[DocumentChunk]:

        return (
            self.db.query(DocumentChunk)
            .filter(DocumentChunk.document_id == document_id)
            .order_by(DocumentChunk.chunk_index)
            .all()
        )

    def delete_document(
        self,
        document_id: int,
    ) -> int:

        rows = (
            self.db.query(DocumentChunk)
            .filter(DocumentChunk.document_id == document_id)
            .delete()
        )

        self.db.commit()

        return rows

    def count(
        self,
        document_id: int,
    ) -> int:

        return (
            self.db.query(DocumentChunk)
            .filter(DocumentChunk.document_id == document_id)
            .count()
        )
