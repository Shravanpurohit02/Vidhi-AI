from app.agents.base.agent import BaseAgent
from app.agents.base.context import AgentContext
from app.agents.base.result import AgentResult

from app.legal.research.research_service import LegalResearchService


class ResearchAgent(BaseAgent):

    name = "research"
    description = "Legal research agent"

    def __init__(self):
        self.service = LegalResearchService()

    async def can_handle(
        self,
        query: str,
        context: AgentContext,
    ) -> bool:

        q = query.lower()

        return any(
            word in q
            for word in (
                "research",
                "precedent",
                "judgment",
                "case law",
                "citation",
            )
        )

    async def execute(
        self,
        query: str,
        context: AgentContext,
    ) -> AgentResult:

        response = self.service.research(query)

        return AgentResult(
            success=True,
            message="Research completed.",
            answer=response.answer,
            metadata=response.model_dump(),
        )
