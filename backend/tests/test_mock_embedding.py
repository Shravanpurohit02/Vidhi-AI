from app.ai.embeddings.mock import MockEmbeddingProvider


def test_mock_embedding_metadata():

    provider = MockEmbeddingProvider()

    assert provider.name == "mock"
    assert provider.dimension == 32
    assert provider.health() is True

    vector = provider.embed("hello")

    assert len(vector) == 32
