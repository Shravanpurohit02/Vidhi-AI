from __future__ import annotations
import importlib.util
from app.document_processing.vector_index.provider import VectorIndexProvider


class ElasticsearchProvider(VectorIndexProvider):
    @property
    def name(self):
        return "elasticsearch"

    @property
    def persistent(self):
        return True

    @property
    def supports_metadata(self):
        return True

    def is_available(self):
        return importlib.util.find_spec("elasticsearch") is not None

    def add(self, ids, vectors, metadata=None):
        raise NotImplementedError

    def search(self, vector, k=5):
        raise NotImplementedError

    def delete(self, ids):
        raise NotImplementedError
