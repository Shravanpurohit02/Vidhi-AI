from fastapi import APIRouter
from pydantic import BaseModel

from app.legal.reasoning.reasoning_service import ReasoningService

router = APIRouter(
    prefix="/reasoning",
    tags=["Legal Reasoning"],
)

service = ReasoningService()


class ReasoningRequest(BaseModel):
    text: str


@router.post("/analyze")
def analyze(
    request: ReasoningRequest,
):
    return service.analyze(request.text)
