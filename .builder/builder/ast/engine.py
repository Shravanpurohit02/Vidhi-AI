from builder.ast.imports import imports
from builder.ast.symbols import symbols

class ASTEngine:

    def build(self, workspace: str):

        modules = symbols.build(workspace)

        return {
            "modules": modules,
            "imports": imports.build(modules),
        }

engine = ASTEngine()
