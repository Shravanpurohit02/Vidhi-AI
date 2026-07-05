from app.ai.embeddings.loader import load_embeddings
from app.ai.embeddings.registry import registry


class EmbeddingSelector:

    PRIORITY = [
        "mock",
    ]

    def select(self):
        load_embeddings()

        for provider_name in self.PRIORITY:
            try:
                provider = registry.get(provider_name)

                if provider.health():
                    return provider

            except Exception:
                continue

        raise RuntimeError("No embedding provider available.")


selector = EmbeddingSelector()
