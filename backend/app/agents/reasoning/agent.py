from app.agents.base.agent import BaseAgent
from app.agents.base.context import AgentContext
from app.agents.base.result import AgentResult

from app.legal.reasoning.reasoning_service import ReasoningService


class ReasoningAgent(BaseAgent):

    name = "reasoning"
    description = "Legal reasoning agent"

    def __init__(self):
        self.service = ReasoningService()

    async def can_handle(
        self,
        query: str,
        context: AgentContext,
    ) -> bool:

        q = query.lower()

        return any(
            word in q
            for word in (
                "analyse",
                "analyze",
                "reason",
                "reasoning",
                "interpret",
                "explain",
            )
        )

    async def execute(
        self,
        query: str,
        context: AgentContext,
    ) -> AgentResult:

        response = self.service.analyze(query)

        return AgentResult(
            success=True,
            message="Reasoning completed.",
            answer=response.answer,
            metadata=response.model_dump(),
        )
