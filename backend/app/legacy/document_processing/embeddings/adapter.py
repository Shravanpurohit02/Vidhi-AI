from __future__ import annotations

from app.document_processing.embeddings.factory import EmbeddingFactory
from app.document_processing.embeddings.registry import EmbeddingRegistry


class EmbeddingAdapter:
    """Facade for embedding generation."""

    def __init__(self, registry: EmbeddingRegistry):
        self.factory = EmbeddingFactory(registry)

    def embed(
        self,
        text: str,
        provider: str | None = None,
    ) -> dict:

        engine = self.factory.create(provider)

        vector = engine.embed(text)

        return {
            "provider": engine.name,
            "dimensions": engine.dimensions,
            "vector": vector,
        }

    def embed_batch(
        self,
        texts: list[str],
        provider: str | None = None,
    ) -> dict:

        engine = self.factory.create(provider)

        vectors = engine.embed_batch(texts)

        return {
            "provider": engine.name,
            "dimensions": engine.dimensions,
            "vectors": vectors,
        }
