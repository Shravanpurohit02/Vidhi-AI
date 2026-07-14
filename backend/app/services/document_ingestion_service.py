from __future__ import annotations

from sqlalchemy.orm import Session

from app.document_processing.chunking.pipeline import ChunkPipeline
from app.ai.embeddings.service import EmbeddingService
from app.repositories.document_chunk_repository import DocumentChunkRepository
from app.repositories.document_embedding_repository import (
    DocumentEmbeddingRepository,
)


class DocumentIngestionService:

    def __init__(self, db: Session):
        self.db = db
        self.chunk_pipeline = ChunkPipeline()
        self.embedding_service = EmbeddingService()

        self.chunk_repository = DocumentChunkRepository(db)
        self.embedding_repository = DocumentEmbeddingRepository(db)

    def ingest(
        self,
        *,
        document_id: int,
        text: str,
        provider: str | None = None,
    ) -> int:

        chunks = self.chunk_pipeline.process(text)

        for index, chunk in enumerate(chunks):

            chunk_text = (
                chunk["text"]
                if isinstance(chunk, dict)
                else str(chunk)
            )

            stored_chunk = self.chunk_repository.create(
                document_id=document_id,
                chunk_index=index,
                text=chunk_text,
                token_count=len(chunk_text.split()),
                metadata_json=chunk if isinstance(chunk, dict) else {},
            )

            embedding = self.embedding_service.embed(
                chunk_text,
                provider=provider,
            )

            self.embedding_repository.create(
                chunk_id=stored_chunk.id,
                provider=embedding["provider"],
                model=embedding["provider"],
                dimensions=embedding["dimensions"],
                embedding=embedding["vector"],
                metadata_json={},
            )

        return self.chunk_repository.count(document_id)
