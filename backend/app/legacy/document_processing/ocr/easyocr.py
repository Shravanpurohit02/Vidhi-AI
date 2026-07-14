from __future__ import annotations

from pathlib import Path
import importlib.util

from app.document_processing.ocr.provider import OCRProvider


class EasyOCRProvider(OCRProvider):

    @property
    def name(self) -> str:
        return "easyocr"

    @property
    def supports_offline(self) -> bool:
        return True

    @property
    def supports_tables(self) -> bool:
        return False

    def is_available(self) -> bool:
        return importlib.util.find_spec("easyocr") is not None

    def extract_text(self, file_path: str | Path) -> dict:
        if not self.is_available():
            raise RuntimeError("EasyOCR is not installed.")

        import easyocr

        reader = easyocr.Reader(["en"])

        result = reader.readtext(str(file_path), detail=0)

        text = "\n".join(result)

        return {
            "text": text,
            "pages": [{"page": 1, "text": text}],
            "confidence": None,
            "metadata": {
                "provider": self.name,
                "offline": True,
            },
        }
