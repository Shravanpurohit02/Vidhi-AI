from fastapi import APIRouter
from pydantic import BaseModel

from app.legal.research.research_service import LegalResearchService

router = APIRouter(
    prefix="/research",
    tags=["Legal Research"],
)

service = LegalResearchService()


class ResearchRequest(BaseModel):
    question: str


@router.post("/")
def research(request: ResearchRequest):
    return service.research(request.question)


@router.get("/history")
def history():
    return service.get_history()


@router.delete("/history")
def clear_history():
    service.clear_history()
    return {"status": "cleared"}
