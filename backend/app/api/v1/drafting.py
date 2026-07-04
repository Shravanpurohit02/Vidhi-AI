from fastapi import APIRouter, HTTPException

from app.legal.drafting.drafting_service import DraftingService
from app.legal.drafting.schemas.draft_request import (
    DraftRequest,
)
from app.legal.drafting.schemas.draft_response import (
    DraftResponse,
)

router = APIRouter(
    prefix="/drafting",
    tags=["Legal Drafting"],
)

service = DraftingService()


@router.post(
    "/generate",
    response_model=DraftResponse,
)
def generate(
    request: DraftRequest,
):

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
