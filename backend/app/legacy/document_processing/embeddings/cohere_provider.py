from __future__ import annotations
import importlib.util
from app.document_processing.embeddings.provider import EmbeddingProvider


class CohereProvider(EmbeddingProvider):
    @property
    def name(self):
        return "cohere"

    @property
    def dimensions(self):
        return 1024

    @property
    def supports_batch(self):
        return True

    def is_available(self):
        return importlib.util.find_spec("cohere") is not None

    def embed(self, text: str):
        raise NotImplementedError("Cohere embedding pending.")
