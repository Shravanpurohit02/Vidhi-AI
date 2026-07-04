from fastapi import APIRouter

from app.legal.reasoning.reasoning_service import (
    ReasoningService,
)
from app.legal.reasoning.schemas.reasoning_request import (
    ReasoningRequest,
)
from app.legal.reasoning.schemas.reasoning_response import (
    ReasoningResponse,
)

router = APIRouter(
    prefix="/reasoning",
    tags=["Legal Reasoning"],
)

service = ReasoningService()


@router.post(
    "/analyze",
    response_model=ReasoningResponse,
)
def analyze(
    request: ReasoningRequest,
):
    return service.analyze(
        request.text,
    )
