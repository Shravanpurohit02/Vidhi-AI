from __future__ import annotations

import re


class SentenceSplitter:
    """Split text into sentences."""

    PATTERN = re.compile(r"(?<=[.!?])\s+")

    @classmethod
    def split(cls, text: str) -> list[str]:
        if not text:
            return []

        sentences = cls.PATTERN.split(text.strip())

        return [sentence.strip() for sentence in sentences if sentence.strip()]
