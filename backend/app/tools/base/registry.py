from app.tools.base.tool import BaseTool

class ToolRegistry:

    def __init__(self):
        self._tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool):
        self._tools[tool.name] = tool

    def get(self, name: str):
        return self._tools.get(name)

    def all(self):
        return list(self._tools.values())
