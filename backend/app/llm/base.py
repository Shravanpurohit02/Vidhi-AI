from abc import ABC, abstractmethod


class BaseLLM(ABC):

    provider: str = ""

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system: str = "",
    ) -> str:
        ...
