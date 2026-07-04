from app.ai.providers.registry import registry


class ProviderSelector:

    PRIORITY = [
        "nvidia",
        "ollama",
        "mock",
    ]

    def select(self):

        for provider_name in self.PRIORITY:

            try:
                provider = registry.get(provider_name)

                if provider.health():
                    return provider

            except Exception:
                pass

        return registry.get("mock")


selector = ProviderSelector()
