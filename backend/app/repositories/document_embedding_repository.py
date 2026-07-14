from __future__ import annotations

from sqlalchemy.orm import Session

from app.models.document_embedding import DocumentEmbedding


class DocumentEmbeddingRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        *,
        chunk_id: int,
        provider: str,
        model: str,
        dimensions: int,
        embedding: list[float],
        metadata_json: dict | None = None,
    ) -> DocumentEmbedding:

        item = DocumentEmbedding(
            chunk_id=chunk_id,
            provider=provider,
            model=model,
            dimensions=dimensions,
            embedding=embedding,
            metadata_json=metadata_json or {},
        )

        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)

        return item

    def get_by_chunk(
        self,
        chunk_id: int,
    ) -> DocumentEmbedding | None:

        return (
            self.db.query(DocumentEmbedding)
            .filter(DocumentEmbedding.chunk_id == chunk_id)
            .first()
        )

    def list_by_provider(
        self,
        provider: str,
    ) -> list[DocumentEmbedding]:

        return (
            self.db.query(DocumentEmbedding)
            .filter(DocumentEmbedding.provider == provider)
            .all()
        )

    def delete_by_chunk(
        self,
        chunk_id: int,
    ) -> int:

        rows = (
            self.db.query(DocumentEmbedding)
            .filter(DocumentEmbedding.chunk_id == chunk_id)
            .delete()
        )

        self.db.commit()

        return rows

    def count(self) -> int:

        return self.db.query(DocumentEmbedding).count()
