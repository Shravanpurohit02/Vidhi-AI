from __future__ import annotations

from abc import ABC, abstractmethod

from app.document_processing.schemas.vector import (
    VectorRecord,
    VectorSearchRequest,
    VectorSearchResult,
)


class VectorIndexProvider(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def persistent(self) -> bool:
        ...

    @property
    @abstractmethod
    def supports_metadata(self) -> bool:
        ...

    @abstractmethod
    def is_available(self) -> bool:
        ...

    @abstractmethod
    def add(
        self,
        records: list[VectorRecord],
    ) -> None:
        ...

    @abstractmethod
    def search(
        self,
        request: VectorSearchRequest,
    ) -> list[VectorSearchResult]:
        ...

    @abstractmethod
    def delete(
        self,
        chunk_ids: list[int],
    ) -> None:
        ...
