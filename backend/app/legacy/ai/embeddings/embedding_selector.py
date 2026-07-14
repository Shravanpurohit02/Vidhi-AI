from app.ai.embeddings.loader import load_embeddings
from app.ai.embeddings.registry import registry


class EmbeddingSelector:

    PRIORITY = [
        "mock",
    ]

    def select(self):

        load_embeddings()

        for name in self.PRIORITY:

            if not registry.exists(name):
                continue

            provider = registry.get(name)

            if provider.health():
                return provider

        raise RuntimeError("No embedding provider available.")


selector = EmbeddingSelector()
