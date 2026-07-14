from __future__ import annotations

from sqlalchemy.orm import Session

from app.repositories.document_chunk_repository import (
    DocumentChunkRepository,
)


class ChunkStorage:
    """
    Production chunk storage.

    Chunks are persisted in the database instead of JSON files.
    """

    def __init__(self, db: Session):
        self.repository = DocumentChunkRepository(db)

    def save(
        self,
        document_id: int,
        chunks: list[dict],
    ) -> int:

        self.repository.delete_document(document_id)

        for index, chunk in enumerate(chunks):

            if isinstance(chunk, dict):
                text = chunk.get("text", "")
                metadata = dict(chunk)
            else:
                text = str(chunk)
                metadata = {}

            self.repository.create(
                document_id=document_id,
                chunk_index=index,
                text=text,
                token_count=len(text.split()),
                page_number=metadata.get("page_number"),
                section=metadata.get("section"),
                metadata_json=metadata,
            )

        return self.repository.count(document_id)

    def load(
        self,
        document_id: int,
    ) -> list[dict]:

        records = self.repository.list_by_document(document_id)

        return [
            {
                "id": row.id,
                "document_id": row.document_id,
                "chunk_index": row.chunk_index,
                "text": row.text,
                "token_count": row.token_count,
                "page_number": row.page_number,
                "section": row.section,
                "metadata": row.metadata_json,
            }
            for row in records
        ]

    def delete(
        self,
        document_id: int,
    ) -> int:

        return self.repository.delete_document(document_id)
