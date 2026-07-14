from __future__ import annotations

from app.document_processing.schemas.vector import (
    VectorRecord,
    VectorSearchRequest,
    VectorSearchResult,
)
from app.document_processing.vector_index.factory import VectorIndexFactory
from app.document_processing.vector_index.registry import VectorIndexRegistry


class VectorIndexAdapter:

    def __init__(self, registry: VectorIndexRegistry):
        self.factory = VectorIndexFactory(registry)

    def add(
        self,
        records: list[VectorRecord],
        provider: str | None = None,
    ) -> None:
        self.factory.create(provider).add(records)

    def search(
        self,
        request: VectorSearchRequest,
    ) -> list[VectorSearchResult]:
        return self.factory.create(request.provider).search(request)

    def delete(
        self,
        chunk_ids: list[int],
        provider: str | None = None,
    ) -> None:
        self.factory.create(provider).delete(chunk_ids)
