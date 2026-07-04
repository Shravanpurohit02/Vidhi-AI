from app.agents.base.agent import BaseAgent
from app.agents.base.context import AgentContext
from app.agents.base.result import AgentResult
from app.agents.court.parser import CourtIntentParser
from app.tools.court.search_tool import CourtSearchTool


class CourtAgent(BaseAgent):

    name = "court"

    description = "Handles court search, import and synchronization."

    def __init__(self):
        self.parser = CourtIntentParser()
        self.search_tool = CourtSearchTool()

    async def can_handle(
        self,
        query: str,
        context: AgentContext,
    ) -> bool:
        keywords = (
            "case",
            "court",
            "cnr",
            "hearing",
            "judge",
            "order",
            "judgment",
            "import",
        )

        return any(k in query.lower() for k in keywords)

    async def execute(
        self,
        query: str,
        context: AgentContext,
    ) -> AgentResult:

        intent = self.parser.parse(query)

        if intent.intent == "search_by_cnr":
            return await self.search_tool.execute(
                cnr=intent.cnr,
            )

        if intent.intent == "search_by_case":
            return await self.search_tool.execute(
                case_number=intent.case_number,
                year=intent.year,
            )

        return AgentResult(
            success=False,
            message="Court request understood but not yet implemented.",
            data={
                "intent": intent.intent,
            },
        )
