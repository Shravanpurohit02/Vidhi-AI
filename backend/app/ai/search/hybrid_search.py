from app.ai.bm25.bm25 import BM25Search
from app.ai.ranking.hybrid_ranker import HybridRanker
from app.ai.reranker.reranker import Reranker
from app.ai.storage.vector_store import PersistentVectorStore


class HybridSearch:

    def __init__(self):

        self.store = PersistentVectorStore()
        self.reranker = Reranker()
        self.bm25 = BM25Search()
        self.hybrid = HybridRanker()

    def search(
        self,
        query,
    ):

        semantic = self.store.all()

        lexical = self.bm25.search(
            query,
            semantic,
        )

        merged = self.hybrid.combine(
            lexical,
            semantic,
        )

        return self.reranker.rerank(
            query,
            merged,
        )
