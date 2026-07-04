from app.ai.embeddings.mock import MockEmbeddingProvider
from app.ai.embeddings.registry import registry


def load_embeddings():

    providers = [
        MockEmbeddingProvider(),
    ]

    for provider in providers:

        name = provider.name

        try:
            registry.get(name)
        except ValueError:
            registry.register(
                name,
                provider,
            )
