from __future__ import annotations

from pathlib import Path
import importlib.util

from app.document_processing.ocr.provider import OCRProvider


class AWSTextractProvider(OCRProvider):

    @property
    def name(self) -> str:
        return "aws_textract"

    @property
    def supports_offline(self) -> bool:
        return False

    @property
    def supports_tables(self) -> bool:
        return True

    def is_available(self) -> bool:
        return importlib.util.find_spec("boto3") is not None

    def extract_text(self, file_path: str | Path) -> dict:
        if not self.is_available():
            raise RuntimeError("boto3 is not installed.")

        return {
            "text": "",
            "pages": [],
            "confidence": None,
            "metadata": {
                "provider": self.name,
                "cloud": True,
            },
        }
