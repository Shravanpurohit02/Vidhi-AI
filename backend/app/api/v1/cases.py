from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.auth.rbac import require_permission
from app.database.database import get_db
from app.models.user import User
from app.schemas.case import CaseCreate, CaseUpdate, CaseResponse
from app.services.case_service import CaseService

router = APIRouter(prefix="/cases", tags=["Cases"])


@router.post("/", response_model=CaseResponse, status_code=201)
def create_case(
    case: CaseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    _: User = Depends(require_permission("cases")),
):
    try:
        data = case.model_dump()
        data["owner_id"] = current_user.id
        data["status"] = "Draft"
        return CaseService.create_case(db, data)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))


@router.get("/", response_model=list[CaseResponse])
def list_cases(db: Session = Depends(get_db)):
    return CaseService.list_cases(db)


@router.get("/search", response_model=list[CaseResponse])
def search_cases(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    return CaseService.search_cases(db, q)


@router.get("/statistics")
def case_statistics(
    db: Session = Depends(get_db),
):
    return CaseService.get_statistics(db)


@router.get("/status/{status}", response_model=list[CaseResponse])
def filter_cases_by_status(
    status: str,
    db: Session = Depends(get_db),
):
    return CaseService.filter_by_status(db, status)


@router.get("/{case_id}", response_model=CaseResponse)
def get_case(case_id: int, db: Session = Depends(get_db)):
    try:
        return CaseService.get_case(db, case_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.put("/{case_id}", response_model=CaseResponse)
def update_case(
    case_id: int,
    case: CaseUpdate,
    db: Session = Depends(get_db),
):
    try:
        return CaseService.update_case(
            db,
            case_id,
            case.model_dump(),
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.delete("/{case_id}")
def delete_case(case_id: int, db: Session = Depends(get_db)):
    try:
        CaseService.delete_case(db, case_id)
        return {"message": "Case deleted successfully"}
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
