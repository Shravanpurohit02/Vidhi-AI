from __future__ import annotations
import importlib.util
from app.document_processing.embeddings.provider import EmbeddingProvider


class OpenAIProvider(EmbeddingProvider):

    @property
    def name(self):
        return "openai"

    @property
    def dimensions(self):
        return 1536

    @property
    def supports_batch(self):
        return True

    def is_available(self):
        try:
            return importlib.util.find_spec("openai") is not None
        except ModuleNotFoundError:
            return False

    def embed(self, text: str):
        raise NotImplementedError("OpenAI embedding implementation pending.")
