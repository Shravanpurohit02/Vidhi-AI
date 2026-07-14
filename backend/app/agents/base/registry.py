from __future__ import annotations

from typing import Iterator

from app.agents.base.agent import BaseAgent
from app.agents.base.exceptions import (
    AgentRegistrationError,
    AgentNotFoundError,
)


class AgentRegistry:

    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}

    @property
    def agents(self) -> list[BaseAgent]:
        """
        Backward-compatible API used by the existing router.
        """
        return list(self._agents.values())

    def register(
        self,
        agent: BaseAgent,
    ) -> None:

        if agent.name in self._agents:
            raise AgentRegistrationError(f"Agent '{agent.name}' is already registered.")

        self._agents[agent.name] = agent

    def unregister(
        self,
        name: str,
    ) -> None:
        self._agents.pop(name, None)

    def get(
        self,
        name: str,
    ) -> BaseAgent:

        if name not in self._agents:
            raise AgentNotFoundError(f"Agent '{name}' not found.")

        return self._agents[name]

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._agents

    def all(self) -> list[BaseAgent]:
        return list(self._agents.values())

    def names(self) -> list[str]:
        return sorted(self._agents.keys())

    def clear(self) -> None:
        self._agents.clear()

    def __iter__(self) -> Iterator[BaseAgent]:
        return iter(self._agents.values())

    def __len__(self) -> int:
        return len(self._agents)


registry = AgentRegistry()
