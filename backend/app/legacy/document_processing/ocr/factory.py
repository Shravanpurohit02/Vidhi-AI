from __future__ import annotations

from app.document_processing.ocr.provider import OCRProvider
from app.document_processing.ocr.registry import OCRRegistry


class OCRFactory:
    """Factory for selecting OCR providers."""

    def __init__(self, registry: OCRRegistry):
        self.registry = registry

    def create(self, preferred: str | None = None) -> OCRProvider:
        if preferred:
            provider = self.registry.get(preferred)
            if provider.is_available():
                return provider

        for name in self.registry.available():
            return self.registry.get(name)

        raise RuntimeError("No OCR provider is available.")
