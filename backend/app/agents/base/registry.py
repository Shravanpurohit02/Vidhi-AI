from app.agents.base.agent import BaseAgent


class AgentRegistry:

    def __init__(self):
        self._agents: list[BaseAgent] = []

    def register(self, agent: BaseAgent):
        self._agents.append(agent)

    @property
    def agents(self):
        return self._agents
