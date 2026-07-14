from __future__ import annotations

import re


class TextCleaner:
    """Normalize OCR and parsed text."""

    @staticmethod
    def clean(text: str) -> str:
        if not text:
            return ""

        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")
        text = text.replace("\t", " ")

        text = re.sub(r"[ ]{2,}", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()
