from __future__ import annotations

from app.ai.bm25.engine import BM25Engine
from app.ai.retrieval.retriever import Retriever
from app.document_processing.semantic_search.rrf import (
    ReciprocalRankFusion,
)


class HybridSearchService:

    def __init__(self):

        self.vector = Retriever()
        self.bm25 = BM25Engine()
        self.rrf = ReciprocalRankFusion()

    def search(
        self,
        query: str,
        top_k: int = 10,
    ):

        lexical = self.bm25.search(
            query=query,
            top_k=top_k,
        )

        semantic = self.vector.retrieve(
            query=query,
            top_k=top_k,
        )

        return self.rrf.fuse(
            lexical=lexical,
            semantic=semantic,
        )
