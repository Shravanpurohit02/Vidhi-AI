from __future__ import annotations

from pathlib import Path
import shutil

from app.document_processing.ocr.provider import OCRProvider


class TesseractProvider(OCRProvider):

    @property
    def name(self) -> str:
        return "tesseract"

    @property
    def supports_offline(self) -> bool:
        return True

    @property
    def supports_tables(self) -> bool:
        return False

    def is_available(self) -> bool:
        return shutil.which("tesseract") is not None

    def extract_text(self, file_path: str | Path) -> dict:
        if not self.is_available():
            raise RuntimeError("Tesseract OCR is not installed.")

        import pytesseract
        from PIL import Image

        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)

        return {
            "text": text,
            "pages": [{"page": 1, "text": text}],
            "confidence": None,
            "metadata": {
                "provider": self.name,
                "offline": True,
            },
        }
