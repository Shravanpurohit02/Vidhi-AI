from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class OCRProvider(ABC):
    """Base interface for all OCR providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable provider name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def supports_offline(self) -> bool:
        """Whether the provider works without internet."""
        raise NotImplementedError

    @property
    @abstractmethod
    def supports_tables(self) -> bool:
        """Whether the provider can recognize tabular layouts."""
        raise NotImplementedError

    @abstractmethod
    def is_available(self) -> bool:
        """Return True if the provider is installed/configured."""
        raise NotImplementedError

    @abstractmethod
    def extract_text(self, file_path: str | Path) -> dict:
        """
        Returns:
        {
            "text": str,
            "pages": list,
            "confidence": float | None,
            "metadata": dict,
        }
        """
        raise NotImplementedError
