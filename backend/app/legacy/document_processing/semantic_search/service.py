from __future__ import annotations

from app.document_processing.semantic_search.pipeline import (
    SemanticSearchPipeline,
)
from app.document_processing.semantic_search.request import SearchRequest


class SemanticSearchService:

    def __init__(self):
        self.pipeline = SemanticSearchPipeline()

    def search(
        self,
        query: str,
        top_k: int = 5,
        provider: str | None = None,
    ) -> dict:

        request = SearchRequest(
            query=query,
            top_k=top_k,
            provider=provider,
        )

        return self.pipeline.search(request)
