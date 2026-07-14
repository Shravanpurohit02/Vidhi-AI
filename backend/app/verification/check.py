from __future__ import annotations

from abc import ABC, abstractmethod

from app.verification.result import VerificationResult


class VerificationCheck(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def run(self) -> VerificationResult:
        ...
