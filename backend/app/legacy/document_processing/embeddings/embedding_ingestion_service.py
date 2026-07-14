from __future__ import annotations

from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.document_chunk import DocumentChunk
from app.models.document_embedding import DocumentEmbedding

from app.document_processing.embeddings.service import EmbeddingService
from app.document_processing.schemas.vector import VectorRecord
from app.document_processing.vector_index.service import VectorIndexService


class EmbeddingIngestionService:

    def __init__(self):

        self.embeddings = EmbeddingService()
        self.index = VectorIndexService()

    def ingest(
        self,
        chunks: list[DocumentChunk],
    ) -> None:

        db: Session = SessionLocal()

        try:

            vector_records = []

            for chunk in chunks:

                result = self.embeddings.embed(chunk.text)

                embedding = DocumentEmbedding(
                    chunk_id=chunk.id,
                    provider=result["provider"],
                    model=result["provider"],
                    dimensions=result["dimensions"],
                    embedding=result["vector"],
                    metadata_json=chunk.metadata_json,
                )

                db.add(embedding)
                db.flush()

                vector_records.append(
                    VectorRecord(
                        document_id=chunk.document_id,
                        chunk_id=chunk.id,
                        provider=result["provider"],
                        model=result["provider"],
                        dimensions=result["dimensions"],
                        vector=result["vector"],
                        metadata=chunk.metadata_json,
                    )
                )

            db.commit()

            self.index.add(vector_records)

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()
