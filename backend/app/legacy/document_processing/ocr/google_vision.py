from __future__ import annotations

from pathlib import Path
import importlib.util

from app.document_processing.ocr.provider import OCRProvider


class GoogleVisionProvider(OCRProvider):

    @property
    def name(self) -> str:
        return "google_vision"

    @property
    def supports_offline(self) -> bool:
        return False

    @property
    def supports_tables(self) -> bool:
        return True

    def is_available(self) -> bool:
        return importlib.util.find_spec("google.cloud.vision") is not None

    def extract_text(self, file_path: str | Path) -> dict:
        if not self.is_available():
            raise RuntimeError("Google Vision SDK is not installed.")

        from google.cloud import vision

        client = vision.ImageAnnotatorClient()

        with open(file_path, "rb") as f:
            image = vision.Image(content=f.read())

        response = client.document_text_detection(image=image)

        text = response.full_text_annotation.text

        return {
            "text": text,
            "pages": [{"page": 1, "text": text}],
            "confidence": None,
            "metadata": {
                "provider": self.name,
                "cloud": True,
            },
        }
