from app.ai.embeddings.mock import MockEmbeddingProvider
from app.ai.embeddings.registry import registry


def _register(provider):
    if not registry.exists(provider.name):
        registry.register(
            provider.name,
            provider,
        )


def load_embeddings() -> None:

    providers = (MockEmbeddingProvider(),)

    for provider in providers:
        try:
            _register(provider)
        except Exception as exc:
            print(exc)
