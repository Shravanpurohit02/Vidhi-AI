from __future__ import annotations

from app.ai.integration.tool_registry import ToolRegistry


class ToolExecutor:

    def __init__(self):
        self.registry = ToolRegistry()

    def execute(
        self,
        tool_name: str,
        *args,
        **kwargs,
    ):

        tool = self.registry.get(tool_name)

        if callable(tool):
            return tool(*args, **kwargs)

        raise RuntimeError(f"Tool '{tool_name}' is not callable.")
