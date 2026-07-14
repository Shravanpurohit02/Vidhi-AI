import os
import shutil
from uuid import uuid4

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.branding_repository import BrandingRepository

router = APIRouter(
    prefix="/branding",
    tags=["Branding Upload"],
)

LOGO_DIR = "storage/logo"
SIGNATURE_DIR = "storage/signature"

os.makedirs(LOGO_DIR, exist_ok=True)
os.makedirs(SIGNATURE_DIR, exist_ok=True)


def save_file(upload: UploadFile, folder: str):
    filename = upload.filename or ""
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""

    if ext not in ("png", "jpg", "jpeg"):
        raise HTTPException(status_code=400, detail="Only PNG/JPG images are allowed.")

    filename = f"{uuid4().hex}.{ext}"
    path = os.path.join(folder, filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(upload.file, buffer)

    return path


@router.post("/logo")
def upload_logo(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    branding = BrandingRepository.get(db)

    if branding is None:
        raise HTTPException(404, "Branding not configured.")

    branding.logo_path = save_file(file, LOGO_DIR)

    db.commit()
    db.refresh(branding)

    return {
        "message": "Logo uploaded successfully.",
        "logo_path": branding.logo_path,
    }


@router.post("/signature")
def upload_signature(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    branding = BrandingRepository.get(db)

    if branding is None:
        raise HTTPException(404, "Branding not configured.")

    branding.signature_path = save_file(file, SIGNATURE_DIR)

    db.commit()
    db.refresh(branding)

    return {
        "message": "Signature uploaded successfully.",
        "signature_path": branding.signature_path,
    }
