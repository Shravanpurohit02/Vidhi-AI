from abc import ABC, abstractmethod
from typing import Any

from app.tools.base.result import ToolResult


class BaseTool(ABC):

    name: str = ""
    description: str = ""

    @abstractmethod
    async def execute(self, **kwargs: Any) -> ToolResult: ...
