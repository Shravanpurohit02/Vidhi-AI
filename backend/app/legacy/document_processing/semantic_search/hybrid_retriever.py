from __future__ import annotations

from app.document_processing.semantic_search.request import SearchRequest
from app.document_processing.semantic_search.result import SearchResult
from app.document_processing.semantic_search.vector_retriever import VectorRetriever


class HybridRetriever:

    def __init__(self):
        self.vector = VectorRetriever()

    def retrieve(
        self,
        request: SearchRequest,
    ) -> list[SearchResult]:
        return self.vector.retrieve(request)
