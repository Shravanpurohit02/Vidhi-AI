from __future__ import annotations

from app.document_processing.ocr.provider import OCRProvider


class OCRRegistry:
    """Registry for OCR providers."""

    def __init__(self) -> None:
        self._providers: dict[str, OCRProvider] = {}

    def register(self, provider: OCRProvider) -> None:
        self._providers[provider.name.lower()] = provider

    def unregister(self, name: str) -> None:
        self._providers.pop(name.lower(), None)

    def get(self, name: str) -> OCRProvider:
        key = name.lower()

        if key not in self._providers:
            raise ValueError(f"OCR provider '{name}' is not registered.")

        return self._providers[key]

    def available(self) -> list[str]:
        return sorted(
            provider.name
            for provider in self._providers.values()
            if provider.is_available()
        )

    def all(self) -> list[str]:
        return sorted(provider.name for provider in self._providers.values())
