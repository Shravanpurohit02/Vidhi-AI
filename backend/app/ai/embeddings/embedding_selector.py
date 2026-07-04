from app.ai.embeddings.registry import registry


class EmbeddingSelector:

    PRIORITY = [
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

        raise RuntimeError(
            "No embedding provider available."
        )


selector = EmbeddingSelector()
