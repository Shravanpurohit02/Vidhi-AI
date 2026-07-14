from __future__ import annotations

from app.document_processing.vector_index.registry import VectorIndexRegistry


class VectorIndexFactory:

    def __init__(self, registry: VectorIndexRegistry):
        self.registry = registry

    def create(self, preferred: str | None = None):
        if preferred:
            provider = self.registry.get(preferred)
            if provider.is_available():
                return provider

        for name in self.registry.available():
            return self.registry.get(name)

        raise RuntimeError("No vector index provider available.")
