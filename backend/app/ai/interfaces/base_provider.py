from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from typing import Any


class BaseAIProvider(ABC):
    """
    Base interface for every AI provider.

    Existing providers remain compatible because only
    generate() is abstract.
    """

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def model(self) -> str: ...

    @property
    def supports_streaming(self) -> bool:
        return False

    @property
    def supports_embeddings(self) -> bool:
        return False

    @property
    def supports_reranking(self) -> bool:
        return False

    @property
    def supports_json_mode(self) -> bool:
        return False

    @property
    def supports_tools(self) -> bool:
        return False

    @property
    def capabilities(self) -> dict[str, bool]:
        return {
            "streaming": self.supports_streaming,
            "embeddings": self.supports_embeddings,
            "reranking": self.supports_reranking,
            "json_mode": self.supports_json_mode,
            "tools": self.supports_tools,
        }

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        **kwargs: Any,
    ) -> str: ...

    async def stream(
        self,
        prompt: str,
        system_prompt: str | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[str]:
        yield self.generate(
            prompt=prompt,
            system_prompt=system_prompt,
            **kwargs,
        )

    def embed(
        self,
        text: str,
    ) -> list[float]:
        raise NotImplementedError(f"{self.name} does not support embeddings.")

    def rerank(
        self,
        query: str,
        documents: list[str],
    ) -> list[int]:
        raise NotImplementedError(f"{self.name} does not support reranking.")

    def health(self) -> bool:
        return True
