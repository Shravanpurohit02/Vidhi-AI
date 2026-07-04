from abc import ABC, abstractmethod


class BaseAIProvider(ABC):
    """
    Base interface for every AI provider.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique provider name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def model(self) -> str:
        """Default model used by this provider."""
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        """Generate a response."""
        raise NotImplementedError

    def health(self) -> bool:
        """
        Returns whether the provider is available.
        Providers may override this.
        """
        return True
