from __future__ import annotations

from pathlib import Path
from hashlib import sha256
from datetime import datetime


class MetadataExtractor:
    """Extract filesystem metadata for uploaded documents."""

    @staticmethod
    def extract(path: str | Path) -> dict:
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        stat = path.stat()

        file_hash = sha256(path.read_bytes()).hexdigest()

        return {
            "filename": path.name,
            "extension": path.suffix.lower(),
            "mime_hint": path.suffix.lower(),
            "size_bytes": stat.st_size,
            "sha256": file_hash,
            "created_at": datetime.fromtimestamp(stat.st_ctime).isoformat(),
            "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "absolute_path": str(path.resolve()),
        }
