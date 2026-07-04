from abc import ABC, abstractmethod


class BaseEmbeddingProvider(ABC):
    """
    Base interface for all embedding providers.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def dimension(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def embed(
        self,
        text: str,
    ) -> list[float]:
        raise NotImplementedError

    def health(self) -> bool:
        return True
