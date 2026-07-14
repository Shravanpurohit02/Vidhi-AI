from __future__ import annotations

from app.ai.search.service import HybridSearch


class RAGPipeline:

    def __init__(self):
        self.search = HybridSearch()

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        provider: str | None = None,
    ) -> dict:
        return self.search.search(
            query=query,
            top_k=top_k,
            provider=provider,
        )
