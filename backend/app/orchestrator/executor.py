from app.agents.base.context import AgentContext
from app.orchestrator.router import AgentRouter


class AgentExecutor:

    def __init__(self, router: AgentRouter):
        self.router = router

    async def execute(
        self,
        query: str,
        context: AgentContext,
    ):
        agent = await self.router.route(query, context)

        if agent is None:
            return {
                "success": False,
                "message": "No suitable agent found.",
            }

        result = await agent.execute(query, context)

        return {
            "agent": agent.name,
            "success": result.success,
            "message": result.message,
            "answer": result.answer,
            "sources": result.sources,
            "tool_calls": result.tool_calls,
            "metadata": result.metadata,
            "data": result.data,
        }
