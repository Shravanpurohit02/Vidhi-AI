from __future__ import annotations

from app.document_processing.semantic_search.result import SearchResult


class Reranker:

    def rerank(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:
        return sorted(
            results,
            key=lambda item: item.score,
            reverse=True,
        )
