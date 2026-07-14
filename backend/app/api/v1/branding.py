from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.branding import (
    BrandingCreate,
    BrandingResponse,
    BrandingUpdate,
)
from app.services.branding_service import BrandingService

router = APIRouter(
    prefix="/branding",
    tags=["Branding"],
)


@router.get(
    "",
    response_model=BrandingResponse | None,
)
def get_branding(
    db: Session = Depends(get_db),
):
    return BrandingService.get(db)


@router.post(
    "",
    response_model=BrandingResponse,
)
def create_branding(
    data: BrandingCreate,
    db: Session = Depends(get_db),
):
    return BrandingService.save(
        db,
        data.model_dump(),
    )


@router.put(
    "",
    response_model=BrandingResponse,
)
def update_branding(
    data: BrandingUpdate,
    db: Session = Depends(get_db),
):
    return BrandingService.update(
        db,
        data.model_dump(exclude_unset=True),
    )


@router.delete("")
def delete_branding(
    db: Session = Depends(get_db),
):
    BrandingService.delete(db)

    return {"success": True, "message": "Branding deleted successfully."}
