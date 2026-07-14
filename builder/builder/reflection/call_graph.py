import ast
from pathlib import Path

from builder.reflection.models import (
    CallEdge,
    CallSite,
)


class _CallCollector(ast.NodeVisitor):

    def __init__(self, module, path):
        self.module = module
        self.path = path
        self.cls = ""
        self.func = ""
        self.edges = []

    def visit_ClassDef(self, node):
        previous = self.cls
        self.cls = node.name
        self.generic_visit(node)
        self.cls = previous

    def visit_FunctionDef(self, node):
        previous = self.func
        self.func = node.name
        self.generic_visit(node)
        self.func = previous

    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):
            callee = node.func.id

        elif isinstance(node.func, ast.Attribute):
            callee = node.func.attr

        else:
            self.generic_visit(node)
            return

        self.edges.append(
            CallEdge(
                caller=CallSite(
                    module=self.module,
                    path=self.path,
                    function=self.func,
                    cls=self.cls,
                    line=getattr(node, "lineno", 0),
                ),
                callee=callee,
            )
        )

        self.generic_visit(node)


class CallGraphBuilder:

    def build(self, workspace: str):

        graph = {}

        root = Path(workspace)

        for file in root.rglob("*.py"):

            try:
                tree = ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore",
                    )
                )
            except Exception:
                continue

            module = ".".join(
                file.relative_to(root).with_suffix("").parts
            )

            visitor = _CallCollector(
                module=module,
                path=str(file),
            )

            visitor.visit(tree)

            graph[module] = visitor.edges

        return graph


call_graph = CallGraphBuilder()
