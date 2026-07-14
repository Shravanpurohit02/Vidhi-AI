from app.agents.base.agent import BaseAgent
from app.agents.base.context import AgentContext
from app.agents.base.result import AgentResult

from app.agents.drafting.parser import DraftRequestParser
from app.legal.drafting.drafting_service import DraftingService


class DraftingAgent(BaseAgent):

    name = "drafting"
    description = "Legal drafting agent"

    def __init__(self):
        self.parser = DraftRequestParser()
        self.service = DraftingService()

    async def can_handle(
        self,
        query: str,
        context: AgentContext,
    ) -> bool:

        q = query.lower()

        return any(
            word in q
            for word in (
                "draft",
                "petition",
                "application",
                "notice",
                "affidavit",
                "agreement",
                "contract",
                "reply",
                "written statement",
                "legal notice",
            )
        )

    async def execute(
        self,
        query: str,
        context: AgentContext,
    ) -> AgentResult:

        request = self.parser.parse(query)

        response = self.service.generate(
            template=request.template,
            facts=request.facts,
            relief=request.relief,
        )

        return AgentResult(
            success=True,
            message="Draft generated.",
            answer=response.document,
            metadata=response.model_dump(),
        )
