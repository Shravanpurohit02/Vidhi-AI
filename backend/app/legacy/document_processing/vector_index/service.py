from __future__ import annotations

from app.document_processing.schemas.vector import (
    VectorRecord,
    VectorSearchRequest,
    VectorSearchResult,
)
from app.document_processing.vector_index.adapter import VectorIndexAdapter
from app.document_processing.vector_index.bootstrap import build_registry


class VectorIndexService:

    def __init__(self):
        self.registry = build_registry()
        self.adapter = VectorIndexAdapter(self.registry)

    def add(
        self,
        records: list[VectorRecord],
        provider: str | None = None,
    ) -> None:
        self.adapter.add(records, provider)

    def search(
        self,
        request: VectorSearchRequest,
    ) -> list[VectorSearchResult]:
        return self.adapter.search(request)

    def delete(
        self,
        chunk_ids: list[int],
        provider: str | None = None,
    ) -> None:
        self.adapter.delete(chunk_ids, provider)

    def providers(self):
        return self.registry.available()
