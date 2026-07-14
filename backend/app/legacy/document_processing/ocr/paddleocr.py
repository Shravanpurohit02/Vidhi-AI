from __future__ import annotations

from pathlib import Path
import importlib.util

from app.document_processing.ocr.provider import OCRProvider


class PaddleOCRProvider(OCRProvider):

    @property
    def name(self) -> str:
        return "paddleocr"

    @property
    def supports_offline(self) -> bool:
        return True

    @property
    def supports_tables(self) -> bool:
        return True

    def is_available(self) -> bool:
        return importlib.util.find_spec("paddleocr") is not None

    def extract_text(self, file_path: str | Path) -> dict:
        if not self.is_available():
            raise RuntimeError("PaddleOCR is not installed.")

        from paddleocr import PaddleOCR

        ocr = PaddleOCR(use_angle_cls=True)

        result = ocr.ocr(str(file_path))

        text = []

        for page in result:
            for line in page:
                text.append(line[1][0])

        output = "\n".join(text)

        return {
            "text": output,
            "pages": [{"page": 1, "text": output}],
            "confidence": None,
            "metadata": {
                "provider": self.name,
                "offline": True,
            },
        }
