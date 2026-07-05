from app.agents.base.registry import AgentRegistry
from app.agents.court.agent import CourtAgent


def register_agents(registry: AgentRegistry) -> AgentRegistry:
    """
    Register all built-in agents.

    Safe to call once during application startup.
    """
    registry.register(CourtAgent())
    return registry
