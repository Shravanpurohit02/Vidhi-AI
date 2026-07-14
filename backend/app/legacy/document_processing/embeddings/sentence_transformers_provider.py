from __future__ import annotations
import importlib.util
from app.document_processing.embeddings.provider import EmbeddingProvider


class SentenceTransformersProvider(EmbeddingProvider):

    @property
    def name(self):
        return "sentence_transformers"

    @property
    def dimensions(self):
        return 768

    @property
    def supports_batch(self):
        return True

    def is_available(self):
        try:
            return importlib.util.find_spec("sentence_transformers") is not None
        except ModuleNotFoundError:
            return False

    def embed(self, text: str):
        raise NotImplementedError("SentenceTransformer implementation pending.")
