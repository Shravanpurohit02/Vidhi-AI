from __future__ import annotations

from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.document_embedding import DocumentEmbedding
from app.document_processing.schemas.vector import (
    VectorRecord,
    VectorSearchRequest,
    VectorSearchResult,
)
from app.document_processing.vector_index.provider import (
    VectorIndexProvider,
)


class SQLiteProvider(VectorIndexProvider):

    @property
    def name(self) -> str:
        return "sqlite"

    @property
    def persistent(self) -> bool:
        return True

    @property
    def supports_metadata(self) -> bool:
        return True

    def is_available(self) -> bool:
        return True

    def add(
        self,
        records: list[VectorRecord],
    ) -> None:

        db: Session = SessionLocal()

        try:

            for record in records:

                db.add(
                    DocumentEmbedding(
                        chunk_id=record.chunk_id,
                        provider=record.provider,
                        model=record.model,
                        dimensions=record.dimensions,
                        embedding=record.vector,
                        metadata_json=record.metadata,
                    )
                )

            db.commit()

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

    @staticmethod
    def _cosine(
        a: list[float],
        b: list[float],
    ) -> float:

        if not a or not b:
            return 0.0

        dot = sum(x * y for x, y in zip(a, b))

        na = sum(x * x for x in a) ** 0.5
        nb = sum(x * x for x in b) ** 0.5

        if na == 0 or nb == 0:
            return 0.0

        return dot / (na * nb)

    def search(
        self,
        request: VectorSearchRequest,
    ) -> list[VectorSearchResult]:

        db: Session = SessionLocal()

        try:

            embeddings = db.query(DocumentEmbedding).all()

            results = []

            for item in embeddings:

                metadata = item.metadata_json or {}
                filters = request.filters

                if filters.court and metadata.get("court") != filters.court:
                    continue

                if filters.judge and metadata.get("judge") != filters.judge:
                    continue

                if filters.year and metadata.get("year") != filters.year:
                    continue

                if filters.jurisdiction and metadata.get("jurisdiction") != filters.jurisdiction:
                    continue

                if filters.case_type and metadata.get("case_type") != filters.case_type:
                    continue

                if filters.act and metadata.get("act") != filters.act:
                    continue

                if filters.section and metadata.get("section") != filters.section:
                    continue

                score = self._cosine(
                    request.query_vector,
                    item.embedding,
                )

                metadata = dict(item.metadata_json or {})

                metadata["confidence"] = (
                    "high"
                    if score >= 0.85 else
                    "medium"
                    if score >= 0.65 else
                    "low"
                )

                metadata["similarity_score"] = round(score, 4)

                results.append(
                    VectorSearchResult(
                        document_id=item.chunk.document_id,
                        chunk_id=item.chunk_id,
                        score=score,
                        vector=None,
                        metadata=metadata,
                    )
                )

            results.sort(
                key=lambda x: x.score,
                reverse=True,
            )

            return results[: request.top_k]

        finally:
            db.close()

    def delete(
        self,
        chunk_ids: list[int],
    ) -> None:

        db: Session = SessionLocal()

        try:

            db.query(DocumentEmbedding).filter(
                DocumentEmbedding.chunk_id.in_(chunk_ids)
            ).delete(
                synchronize_session=False
            )

            db.commit()

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()
