from __future__ import annotations

import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile, status

STORAGE_DIR = Path("storage/documents")
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # 100 MB

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
}

ALLOWED_CONTENT_TYPES = {
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "text/plain",
}


class FileStorage:

    @staticmethod
    def validate(upload: UploadFile) -> None:
        suffix = Path(upload.filename or "").suffix.lower()

        if suffix not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unsupported file type",
            )

        if upload.content_type not in ALLOWED_CONTENT_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unsupported content type",
            )

        upload.file.seek(0, 2)
        size = upload.file.tell()
        upload.file.seek(0)

        if size == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Empty file",
            )

        if size > MAX_UPLOAD_SIZE:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail="File exceeds maximum upload size",
            )

    @classmethod
    def save(cls, upload: UploadFile):
        cls.validate(upload)

        suffix = Path(upload.filename or "").suffix.lower()

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
        p = Path(path).resolve()

        storage = STORAGE_DIR.resolve()

        if storage not in p.parents:
            raise ValueError("Invalid storage path")

        if p.exists():
            p.unlink()
