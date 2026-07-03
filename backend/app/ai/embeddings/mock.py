from app.ai.embeddings.base import BaseEmbeddingProvider


class MockEmbeddingProvider(BaseEmbeddingProvider):

    def embed(self, text: str):

        value = float(len(text))

        return [value] * 32
