import ast
from pathlib import Path

from builder.ast.module import Module


class Parser:

    def parse(self, path: str):

        source = Path(path).read_text(
            encoding="utf-8",
            errors="ignore",
        )

        tree = ast.parse(source)

        module = Module(path=path)

        module.line_count = len(source.splitlines())
        module.docstring = ast.get_docstring(tree) or ""

        for node in tree.body:

            if isinstance(node, ast.ClassDef):
                module.classes.append(node.name)

                for dec in node.decorator_list:
                    if isinstance(dec, ast.Name):
                        module.decorators.append(dec.id)

            elif isinstance(node, ast.FunctionDef):
                module.functions.append(node.name)

                for dec in node.decorator_list:
                    if isinstance(dec, ast.Name):
                        module.decorators.append(dec.id)

            elif isinstance(node, ast.AsyncFunctionDef):
                module.async_functions.append(node.name)

                for dec in node.decorator_list:
                    if isinstance(dec, ast.Name):
                        module.decorators.append(dec.id)

            elif isinstance(node, ast.Import):
                for alias in node.names:
                    module.imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                module.imports.append(node.module or "")

            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        module.assignments.append(target.id)
                        module.global_variables.append(target.id)

        module.exports = [
            *module.classes,
            *module.functions,
            *module.async_functions,
        ]

        module.symbol_count = (
            len(module.classes)
            + len(module.functions)
            + len(module.async_functions)
            + len(module.global_variables)
        )

        return module


parser = Parser()
