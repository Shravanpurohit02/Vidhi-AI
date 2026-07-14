from __future__ import annotations
import importlib.util
from app.document_processing.embeddings.provider import EmbeddingProvider


class HuggingFaceProvider(EmbeddingProvider):

    @property
    def name(self):
        return "huggingface"

    @property
    def dimensions(self):
        return 768

    @property
    def supports_batch(self):
        return True

    def is_available(self):
        try:
            return importlib.util.find_spec("transformers") is not None
        except ModuleNotFoundError:
            return False

    def embed(self, text: str):
        raise NotImplementedError("Hugging Face embedding implementation pending.")
