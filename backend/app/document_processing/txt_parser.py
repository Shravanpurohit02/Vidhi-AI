from __future__ import annotations

from pathlib import Path


class TXTParser:
    """Production TXT parser with UTF-8 fallback handling."""

    @staticmethod
    def parse(path: str | Path) -> dict:
        path = Path(path)

        encodings = ("utf-8", "utf-8-sig", "latin-1")

        text = None
        encoding_used = None

        for encoding in encodings:
            try:
                text = path.read_text(encoding=encoding)
                encoding_used = encoding
                break
            except UnicodeDecodeError:
                continue

        if text is None:
            raise ValueError("Unable to decode text file.")

        lines = text.splitlines()

        return {
            "file": str(path),
            "encoding": encoding_used,
            "line_count": len(lines),
            "character_count": len(text),
            "text": text,
            "lines": [
                {
                    "line": index + 1,
                    "text": line,
                }
                for index, line in enumerate(lines)
            ],
        }
