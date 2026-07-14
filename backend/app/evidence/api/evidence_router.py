from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.evidence.services.evidence_service import EvidenceService

router = APIRouter(
    prefix="/evidence",
    tags=["Evidence"],
)

service = EvidenceService()

UPLOAD_DIR = Path("storage/evidence")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_evidence(
    file: UploadFile = File(...),
):

    if file.filename is None:
        raise HTTPException(
            status_code=400,
            detail="Filename is required.",
        )

    destination = UPLOAD_DIR / file.filename

    with destination.open("wb") as output:
        while chunk := await file.read(1024 * 1024):
            output.write(chunk)

    record = service.register(
        str(destination),
        {
            "filename": file.filename,
            "content_type": file.content_type,
            "size": destination.stat().st_size,
        },
    )

    return record


@router.get("/{evidence_id}")
def get_evidence(
    evidence_id: str,
):

    record = service.repository.get(evidence_id)

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Evidence not found.",
        )

    return record


@router.delete("/{evidence_id}")
def delete_evidence(
    evidence_id: str,
):

    service.repository.delete(evidence_id)

    return {
        "message": "Evidence deleted successfully.",
    }


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "module": "evidence",
    }
