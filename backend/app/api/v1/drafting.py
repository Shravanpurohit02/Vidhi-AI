from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.legal.drafting.drafting_service import DraftingService

router = APIRouter(
    prefix="/drafting",
    tags=["Legal Drafting"],
)

service = DraftingService()


class DraftRequest(BaseModel):
    template: str
    facts: str
    relief: str = ""


@router.post("/generate")
def generate(request: DraftRequest):

    try:
        return service.generate(
            request.template,
            request.facts,
            request.relief,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )
