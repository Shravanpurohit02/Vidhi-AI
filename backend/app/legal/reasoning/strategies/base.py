from __future__ import annotations

from abc import ABC, abstractmethod


class BaseReasoningStrategy(ABC):

    name = "base"

    @abstractmethod
    def build_reasoning(
        self,
        answer: str,
        citations: list,
    ) -> str: ...
