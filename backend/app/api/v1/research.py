from fastapi import APIRouter

from app.legal.research.research_service import LegalResearchService
from app.legal.research.schemas.research_request import (
    ResearchRequest,
)
from app.legal.research.schemas.research_response import (
    ResearchResponse,
)

router = APIRouter(
    prefix="/research",
    tags=["Legal Research"],
)

service = LegalResearchService()


@router.post(
    "/",
    response_model=ResearchResponse,
)
def research(
    request: ResearchRequest,
):
    return service.research(
        request.question,
    )


@router.get("/history")
def history():
    return service.get_history()


@router.delete("/history")
def clear_history():
    service.clear_history()
    return {
        "status": "cleared",
    }
