from app.ai.embeddings.loader import load_embeddings
from app.ai.embeddings.registry import registry


def test_embedding_registry():

    load_embeddings()

    assert "mock" in registry.providers()
