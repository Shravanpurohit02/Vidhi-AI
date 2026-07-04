from app.ai.embeddings.loader import load_embeddings
from app.ai.embeddings.embedding_selector import selector


def test_selector():

    load_embeddings()

    provider = selector.select()

    assert provider.name == "mock"

    vector = provider.embed("Vidhi AI")

    assert len(vector) == provider.dimension
