from __future__ import annotations

from pathlib import Path

from app.document_processing.ocr.factory import OCRFactory
from app.document_processing.ocr.registry import OCRRegistry


class OCRAdapter:
    """Facade for OCR operations."""

    def __init__(self, registry: OCRRegistry):
        self.factory = OCRFactory(registry)

    def extract(
        self,
        file_path: str | Path,
        provider: str | None = None,
    ) -> dict:
        engine = self.factory.create(provider)
        return engine.extract_text(file_path)
