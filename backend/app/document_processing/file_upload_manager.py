from __future__ import annotations

import hashlib
import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile

from app.document_processing.config import (
    ALLOWED_EXTENSIONS,
    DOCUMENTS_DIR,
    MAX_UPLOAD_SIZE,
)


class FileUploadManager:
    @staticmethod
    def save(upload: UploadFile) -> dict:
        if upload.filename is None:
            raise HTTPException(status_code=400, detail="Filename is missing.")

        extension = Path(upload.filename).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file type: {extension}",
            )

        data = upload.file.read()

        if len(data) > MAX_UPLOAD_SIZE:
            raise HTTPException(
                status_code=413,
                detail="File exceeds maximum upload size.",
            )

        sha256 = hashlib.sha256(data).hexdigest()

        filename = f"{uuid4().hex}{extension}"
        destination = DOCUMENTS_DIR / filename

        with destination.open("wb") as f:
            f.write(data)

        upload.file.seek(0)

        return {
            "original_name": upload.filename,
            "stored_name": filename,
            "path": str(destination),
            "extension": extension,
            "size": len(data),
            "sha256": sha256,
        }

    @staticmethod
    def delete(path: str) -> None:
        p = Path(path)
        if p.exists():
            p.unlink()

    @staticmethod
    def copy(source: str, destination: str) -> None:
        shutil.copy2(source, destination)
