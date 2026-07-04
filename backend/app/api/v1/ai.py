from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.base.context import AgentContext
from app.agents.base.registry import AgentRegistry
from app.orchestrator.router import AgentRouter
from app.orchestrator.executor import AgentExecutor


router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


class AIRequest(BaseModel):
    query: str
    user_id: int | None = 1


registry = AgentRegistry()

router_instance = AgentRouter(registry)
executor = AgentExecutor(router_instance)


@router.post("/chat")
async def ai_chat(request: AIRequest):

    context = AgentContext(
        user_id=request.user_id,
    )

    return await executor.execute(
        request.query,
        context,
    )
