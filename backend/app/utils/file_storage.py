from pathlib import Path
import shutil
from uuid import uuid4

from fastapi import UploadFile

STORAGE_DIR = Path("storage/documents")
STORAGE_DIR.mkdir(parents=True, exist_ok=True)


class FileStorage:

    @staticmethod
    def save(upload: UploadFile):
        suffix = Path(upload.filename).suffix.lower()

        filename = f"{uuid4().hex}{suffix}"

        destination = STORAGE_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload.file, buffer)

        return filename, str(destination)

    @staticmethod
    def exists(path: str):
        return Path(path).exists()

    @staticmethod
    def delete(path: str):
        p = Path(path)

        if p.exists():
            p.unlink()
