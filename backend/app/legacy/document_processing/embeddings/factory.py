from __future__ import annotations

from app.document_processing.embeddings.provider import EmbeddingProvider
from app.document_processing.embeddings.registry import EmbeddingRegistry


class EmbeddingFactory:
    """Factory for selecting embedding providers."""

    def __init__(self, registry: EmbeddingRegistry):
        self.registry = registry

    def create(
        self,
        preferred: str | None = None,
    ) -> EmbeddingProvider:

        if preferred:
            provider = self.registry.get(preferred)

            if provider.is_available():
                return provider

        if "mock" in self.registry.all():
            return self.registry.get("mock")

        for name in self.registry.available():
            return self.registry.get(name)

        raise RuntimeError("No embedding provider is available.")
