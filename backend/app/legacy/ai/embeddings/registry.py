from __future__ import annotations

from app.ai.embeddings.base import BaseEmbeddingProvider


class EmbeddingRegistry:
    """
    Registry for embedding providers.
    """

    def __init__(self):
        self._providers: dict[str, BaseEmbeddingProvider] = {}

    def register(
        self,
        name: str,
        provider: BaseEmbeddingProvider,
    ) -> None:
        self._providers[name.lower()] = provider

    def unregister(
        self,
        name: str,
    ) -> None:
        self._providers.pop(name.lower(), None)

    def exists(
        self,
        name: str,
    ) -> bool:
        return name.lower() in self._providers

    def get(
        self,
        name: str,
    ) -> BaseEmbeddingProvider:

        provider = self._providers.get(name.lower())

        if provider is None:
            raise ValueError(f"Embedding provider '{name}' is not registered.")

        return provider

    def all(self) -> list[BaseEmbeddingProvider]:
        return list(self._providers.values())

    def providers(self) -> list[str]:
        return sorted(self._providers.keys())

    def healthy(self) -> list[BaseEmbeddingProvider]:
        healthy: list[BaseEmbeddingProvider] = []

        for provider in self._providers.values():
            try:
                if provider.health():
                    healthy.append(provider)
            except Exception as exc:
                print(exc)

        return healthy

    def clear(self) -> None:
        self._providers.clear()


registry = EmbeddingRegistry()
