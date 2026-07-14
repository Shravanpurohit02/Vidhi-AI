from app.agents.base.context import AgentContext
from app.agents.base.exceptions import AgentExecutionError
from app.orchestrator.router import AgentRouter


class AgentExecutor:

    def __init__(
        self,
        router: AgentRouter,
    ):
        self.router = router

    async def execute(
        self,
        query: str,
        context: AgentContext,
    ) -> dict:

        agent = await self.router.route(query, context)

        if agent is None:
            return {
                "success": False,
                "message": "No suitable agent found.",
            }

        try:
            result = await agent.execute(query, context)

        except AgentExecutionError as exc:
            return {
                "agent": agent.name,
                "success": False,
                "message": str(exc),
            }

        except Exception as exc:
            return {
                "agent": agent.name,
                "success": False,
                "message": f"Unexpected execution error: {exc}",
            }

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
