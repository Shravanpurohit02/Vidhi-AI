from __future__ import annotations
import importlib.util
from app.document_processing.vector_index.provider import VectorIndexProvider


class WeaviateProvider(VectorIndexProvider):
    @property
    def name(self):
        return "weaviate"

    @property
    def persistent(self):
        return True

    @property
    def supports_metadata(self):
        return True

    def is_available(self):
        return importlib.util.find_spec("weaviate") is not None

    def add(self, ids, vectors, metadata=None):
        raise NotImplementedError

    def search(self, vector, k=5):
        raise NotImplementedError

    def delete(self, ids):
        raise NotImplementedError
