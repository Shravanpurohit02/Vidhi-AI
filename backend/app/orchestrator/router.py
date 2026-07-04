from app.agents.base.context import AgentContext
from app.agents.base.registry import AgentRegistry


class AgentRouter:

    def __init__(self, registry: AgentRegistry):
        self.registry = registry

    async def route(
        self,
        query: str,
        context: AgentContext,
    ):
        for agent in self.registry.agents:
            if await agent.can_handle(query, context):
                return agent

        return None
