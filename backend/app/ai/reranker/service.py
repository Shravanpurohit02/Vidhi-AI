from __future__ import annotations

from app.ai.reranker.cross_encoder import CrossEncoder


class RerankerService:

    def __init__(self):
        self.model=CrossEncoder()

    def rerank(
        self,
        query:str,
        results:list,
    ):
        return self.model.rerank(
            query,
            results,
        )
