from abc import ABC, abstractmethod

from app.agents.base.context import AgentContext
from app.agents.base.result import AgentResult


class BaseAgent(ABC):

    name: str = "base"
    description: str = ""

    @abstractmethod
    async def can_handle(
        self,
        query: str,
        context: AgentContext,
    ) -> bool:
        ...

    @abstractmethod
    async def execute(
        self,
        query: str,
        context: AgentContext,
    ) -> AgentResult:
        ...
