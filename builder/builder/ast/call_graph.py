import ast
from pathlib import Path


class CallGraph:

    def build(self, modules):

        graph = {}

        callers = {}

        for module in modules:

            path = module.path

            graph[path] = []

            try:

                source = Path(path).read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

            except Exception:
                continue

            calls = []

            class Visitor(ast.NodeVisitor):

                def visit_Call(self, node):

                    if isinstance(node.func, ast.Name):

                        calls.append(
                            node.func.id
                        )

                    elif isinstance(
                        node.func,
                        ast.Attribute,
                    ):

                        calls.append(
                            node.func.attr
                        )

                    self.generic_visit(node)

            Visitor().visit(tree)

            graph[path] = sorted(
                set(calls)
            )

            for call in graph[path]:

                callers.setdefault(
                    call,
                    [],
                ).append(path)

        return {
            "calls": graph,
            "callers": callers,
        }

    def called_symbols(
        self,
        graph,
        path,
    ):

        return graph["calls"].get(
            path,
            [],
        )

    def callers_of(
        self,
        graph,
        symbol,
    ):

        return graph["callers"].get(
            symbol,
            [],
        )


graph = CallGraph()
