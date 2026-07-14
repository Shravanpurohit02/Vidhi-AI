from __future__ import annotations

from pathlib import Path

from docx import Document


class DOCXParser:
    """Production DOCX parser."""

    @staticmethod
    def parse(path: str | Path) -> dict:
        path = Path(path)

        document = Document(str(path))

        paragraphs = []
        full_text = []

        for index, paragraph in enumerate(document.paragraphs, start=1):
            text = paragraph.text.strip()

            paragraphs.append(
                {
                    "paragraph": index,
                    "text": text,
                    "characters": len(text),
                }
            )

            if text:
                full_text.append(text)

        return {
            "file": str(path),
            "paragraph_count": len(paragraphs),
            "paragraphs": paragraphs,
            "text": "\n".join(full_text),
            "metadata": {
                "title": document.core_properties.title,
                "author": document.core_properties.author,
                "subject": document.core_properties.subject,
                "keywords": document.core_properties.keywords,
                "created": str(document.core_properties.created),
                "modified": str(document.core_properties.modified),
            },
        }
