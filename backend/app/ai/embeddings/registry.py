from app.ai.embeddings.base import BaseEmbeddingProvider


class EmbeddingRegistry:

    def __init__(self):
        self._providers: dict[str, BaseEmbeddingProvider] = {}

    def register(
        self,
        name: str,
        provider: BaseEmbeddingProvider,
    ) -> None:
        self._providers[name.lower()] = provider

    def get(
        self,
        name: str,
    ) -> BaseEmbeddingProvider:

        provider = self._providers.get(name.lower())

        if provider is None:
            raise ValueError(f"Embedding provider '{name}' not registered.")

        return provider

    def providers(self):
        return sorted(self._providers.keys())


registry = EmbeddingRegistry()
