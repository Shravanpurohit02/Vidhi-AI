from __future__ import annotations
from app.document_processing.embeddings.provider import EmbeddingProvider


class MockProvider(EmbeddingProvider):
    @property
    def name(self):
        return "mock"

    @property
    def dimensions(self):
        return 768

    @property
    def supports_batch(self):
        return True

    def is_available(self):
        return True

    def embed(self, text: str) -> list[float]:
        return [0.0] * self.dimensions

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [self.embed(text) for text in texts]
