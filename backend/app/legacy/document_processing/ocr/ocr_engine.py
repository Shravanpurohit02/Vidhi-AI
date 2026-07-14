from __future__ import annotations

class OCREngine:

    def extract(
        self,
        image,
    )->str:

        raise NotImplementedError(
            "OCR provider not configured."
        )
