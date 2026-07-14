from __future__ import annotations


class ToolRegistry:

    def __init__(self):
        self._tools: dict[str, object] = {}

    def register(
        self,
        name: str,
        tool: object,
    ):
        self._tools[name] = tool

    def get(
        self,
        name: str,
    ):
        return self._tools[name]

    def names(self):
        return sorted(self._tools.keys())
