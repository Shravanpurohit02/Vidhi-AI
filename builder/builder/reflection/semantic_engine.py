from builder.intelligence.workspace_index import workspace_indexer

from .reference_index import indexer
from .call_graph import call_graph
from .reverse_index import reverse_index
from .semantic_models import (
    SemanticRepository,
    SemanticSymbol,
)


class SemanticEngine:

    def build(
        self,
        workspace: str,
    ):

        idx = workspace_indexer.build(workspace)

        repo = SemanticRepository()

        repo.modules = idx.dependency_graph
        repo.references = indexer.build(workspace)
        repo.call_graph = call_graph.build(workspace)

        for symbol in idx.symbol_index.symbols:

            key = f"{symbol.module}:{symbol.name}"

            repo.symbols[key] = SemanticSymbol(
                name=symbol.name,
                module=symbol.module,
                kind=symbol.kind,
                line=symbol.line,
                references=repo.references.get(
                    symbol.name,
                    [],
                ),
            )

        
        repo.reverse_index = reverse_index.build(repo)

        return repo
        


engine = SemanticEngine()
