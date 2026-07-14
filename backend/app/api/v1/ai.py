from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.base.context import AgentContext
from app.agents.base.registry import AgentRegistry
from app.agents.court.agent import CourtAgent
from app.ai.services.ai_service import AIService
from app.orchestrator.executor import AgentExecutor
from app.orchestrator.router import AgentRouter

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


class AIRequest(BaseModel):
    query: str | None = None
    message: str | None = None
    user_id: int | None = 1
    conversation_id: str | None = None


class IngestRequest(BaseModel):
    text: str
    metadata: dict[str, Any] = {}


registry = AgentRegistry()
registry.register(CourtAgent())

router_instance = AgentRouter(registry)
executor = AgentExecutor(router_instance)

ai_service = AIService()


@router.post("/ingest")
async def ingest(request: IngestRequest):
    ai_service.ingest_document(
        text=request.text,
        metadata=request.metadata,
    )
    return {
        "success": True,
    }


@router.delete("/memory")
async def clear_memory():
    ai_service.memory.clear()
    return {
        "status": "cleared",
    }


@router.post("/chat")
async def ai_chat(request: AIRequest):

    question = request.query or request.message

    if not question:
        return {
            "success": False,
            "message": "Query is required.",
        }

    context = AgentContext(
        user_id=request.user_id,
        session_id=request.conversation_id,
    )

    orchestrator = await executor.execute(
        question,
        context,
    )

    if orchestrator.get("success"):
        return orchestrator

    result = ai_service.ask(question)

    return {
        "success": True,
        "answer": result["answer"],
        "citations": result["citations"],
    }
