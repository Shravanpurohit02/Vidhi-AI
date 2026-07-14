from __future__ import annotations
import importlib.util
from app.document_processing.embeddings.provider import EmbeddingProvider


class GeminiProvider(EmbeddingProvider):

    @property
    def name(self):
        return "gemini"

    @property
    def dimensions(self):
        return 768

    @property
    def supports_batch(self):
        return True

    def is_available(self):
        try:
            return importlib.util.find_spec("google.generativeai") is not None
        except ModuleNotFoundError:
            return False

    def embed(self, text: str):
        raise NotImplementedError("Gemini embedding implementation pending.")
