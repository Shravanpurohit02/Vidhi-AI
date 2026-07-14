from __future__ import annotations

from abc import ABC, abstractmethod

from app.document_processing.semantic_search.request import SearchRequest
from app.document_processing.semantic_search.result import SearchResult


class Retriever(ABC):

    @abstractmethod
    def retrieve(
        self,
        request: SearchRequest,
    ) -> list[SearchResult]:
        raise NotImplementedError
