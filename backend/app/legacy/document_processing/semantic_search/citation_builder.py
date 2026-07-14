from __future__ import annotations

from app.document_processing.semantic_search.result import SearchResult


class CitationBuilder:

    def build(
        self,
        results: list[SearchResult],
    ) -> list[dict]:

        citations = []

        for item in results:
            citations.append(
                {
                    "document_id": item.document_id,
                    "chunk_id": item.chunk_id,
                    "score": item.score,
                }
            )

        return citations
