"""
Agent bootstrap for Vidhi-AI v1.

Court-related agents are intentionally excluded.
They will be introduced in v2.
"""

from app.agents.base.registry import registry


def bootstrap_agents() -> None:
    """
    Register all built-in v1 agents.
    Safe to call multiple times.
    """

    from app.agents.research.agent import ResearchAgent
    from app.agents.reasoning.agent import ReasoningAgent
    from app.agents.drafting.agent import DraftingAgent

    for agent in (
        ResearchAgent(),
        ReasoningAgent(),
        DraftingAgent(),
    ):
        if not registry.exists(agent.name):
            registry.register(agent)
