from app.ai.interfaces.base_provider import BaseAIProvider


class ProviderRegistry:
    """
    Registry for AI providers.

    Keeps AIService independent of concrete provider
    implementations.
    """

    def __init__(self):
        self._providers: dict[str, BaseAIProvider] = {}

    def register(
        self,
        name: str,
        provider: BaseAIProvider,
    ) -> None:
        self._providers[name.lower()] = provider

    def get(
        self,
        name: str,
    ) -> BaseAIProvider:

        provider = self._providers.get(name.lower())

        if provider is None:
            raise ValueError(
                f"Provider '{name}' is not registered."
            )

        return provider

    def providers(self) -> list[str]:
        return sorted(self._providers.keys())


registry = ProviderRegistry()
