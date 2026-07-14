from __future__ import annotations

from app.ai.bm25.engine import BM25Engine
from app.ai.reranker.service import RerankerService
from app.ai.vectorstore.service import VectorStoreService


class HybridSearch:

    def __init__(self):
        self.vector = VectorStoreService()
        self.bm25 = BM25Engine()
        self.reranker = RerankerService()

    def search(self, query: str, limit: int = 10):
        vector_results = self.vector.search(query, limit=limit)
        keyword_results = self.bm25.search(query, limit=limit)

        merged = list(vector_results) + list(keyword_results)

        return self.reranker.rerank(query, merged)
