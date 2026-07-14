from __future__ import annotations

from app.ai.embeddings.service import EmbeddingService
from app.document_processing.semantic_search.request import SearchRequest
from app.document_processing.semantic_search.result import SearchResult
from app.document_processing.semantic_search.retriever import Retriever
from app.ai.vectorstore.service import VectorStoreService


class VectorRetriever(Retriever):

    def __init__(self):
        self.embeddings = EmbeddingService()
        self.index = VectorStoreService()

    def retrieve(self, request: SearchRequest) -> list[SearchResult]:
        embedding = self.embeddings.embed(
            request.query,
            provider=request.provider,
        )

        matches = self.index.search(
            embedding["vector"],
            k=request.top_k,
        )

        return [
            SearchResult(
                document_id=item.get("document_id", ""),
                chunk_id=item.get("chunk_id", ""),
                score=item.get("score", 0.0),
                text=item.get("text", ""),
                metadata=item.get("metadata", {}),
            )
            for item in matches
        ]
