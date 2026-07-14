from __future__ import annotations

from fastapi import APIRouter

from app.ai.integration.chat_service import ChatService
from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"],
)

service = AIService()


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = service.chat(
        conversation_id=request.conversation_id,
        message=request.message,
        provider=request.provider,
    )

    return ChatResponse(**result)


@router.get("/{conversation_id}")
def history(conversation_id: str):
    return {
        "conversation_id": conversation_id,
        "messages": service.memory.history(conversation_id),
    }


@router.delete("/{conversation_id}")
def delete_history(conversation_id: str):

    service.memory.clear(conversation_id)

    return {"message": "Conversation deleted."}


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "chat",
    }
