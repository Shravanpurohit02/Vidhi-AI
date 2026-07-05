from app.tools.base.tool import BaseTool


class ToolRegistry:

    def __init__(self):
        self._tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool):
        if tool.name in self._tools:
            raise ValueError(f"Tool '{tool.name}' already registered.")

        self._tools[tool.name] = tool

    def get(self, name: str):
        tool = self._tools.get(name)

        if tool is None:
            raise ValueError(f"Unknown tool '{name}'.")

        return tool

    def all(self):
        return list(self._tools.values())
