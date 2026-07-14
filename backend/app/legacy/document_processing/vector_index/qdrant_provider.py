from __future__ import annotations

import importlib.util

from app.document_processing.vector_index.provider import VectorIndexProvider


class QdrantProvider(VectorIndexProvider):

    @property
    def name(self) -> str:
        return "qdrant"

    @property
    def persistent(self) -> bool:
        return True

    @property
    def supports_metadata(self) -> bool:
        return True

    def is_available(self) -> bool:
        return importlib.util.find_spec("qdrant_client") is not None

    def add(self, ids, vectors, metadata=None) -> None:
        raise NotImplementedError

    def search(self, vector, k=5) -> list[dict]:
        raise NotImplementedError

    def delete(self, ids) -> None:
        raise NotImplementedError
