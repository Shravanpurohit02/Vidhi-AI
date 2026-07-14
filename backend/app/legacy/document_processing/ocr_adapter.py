from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class OCRProvider(ABC):
    """Base class for OCR engines."""

    @abstractmethod
    def extract_text(self, file_path: str | Path) -> str:
        raise NotImplementedError


class DummyOCRProvider(OCRProvider):
    """
    Temporary provider.

    Replace with TesseractOCRProvider, PaddleOCRProvider,
    EasyOCRProvider, etc. without changing the pipeline.
    """

    def extract_text(self, file_path: str | Path) -> str:
        return ""


class OCRAdapter:
    def __init__(self, provider: OCRProvider | None = None):
        self.provider = provider or DummyOCRProvider()

    def parse(self, file_path: str | Path) -> dict:
        file_path = Path(file_path)

        text = self.provider.extract_text(file_path)

        return {
            "file": str(file_path),
            "ocr_used": True,
            "provider": self.provider.__class__.__name__,
            "character_count": len(text),
            "text": text,
        }
