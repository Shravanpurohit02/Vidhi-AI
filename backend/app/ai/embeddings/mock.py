from app.ai.embeddings.base import BaseEmbeddingProvider


class MockEmbeddingProvider(BaseEmbeddingProvider):

    @property
    def name(self) -> str:
        return "mock"

    @property
    def dimension(self) -> int:
        return 32

    def embed(
        self,
        text: str,
    ) -> list[float]:

        value = float(len(text))

        return [value] * self.dimension
