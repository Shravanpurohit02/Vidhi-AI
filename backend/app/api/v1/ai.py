from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.services.ai_service import AIService

router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"],
)

service = AIService()


class ChatRequest(BaseModel):
    message: str


class IngestRequest(BaseModel):
    text: str
    metadata: dict = {}


@router.post("/ingest")
def ingest_document(request: IngestRequest):
    service.ingest_document(
        request.text,
        request.metadata,
    )
    return {"status": "indexed"}


@router.post("/chat")
def chat(request: ChatRequest):
    return service.ask(request.message)


@router.delete("/memory")
def clear_memory():
    service.memory.clear()
    return {"status": "cleared"}
