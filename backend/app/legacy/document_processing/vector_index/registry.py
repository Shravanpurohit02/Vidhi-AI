from __future__ import annotations

from app.document_processing.vector_index.provider import VectorIndexProvider


class VectorIndexRegistry:

    def __init__(self):
        self._providers: dict[str, VectorIndexProvider] = {}

    def register(self, provider: VectorIndexProvider):
        self._providers[provider.name] = provider

    def get(self, name: str) -> VectorIndexProvider:
        return self._providers[name]

    def all(self):
        return sorted(self._providers.keys())

    def available(self):
        return sorted(
            name
            for name, provider in self._providers.items()
            if provider.is_available()
        )
