from pathlib import Path

from builder.project_graph.database import database
from builder.project_graph.edge import GraphEdge
from builder.project_graph.node import GraphNode

class GraphIndexer:

    def build(self, workspace: str):
        root = Path(workspace)

        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue

            node = GraphNode(
                path=str(path),
                name=path.name,
                type=path.suffix.lstrip(".") or "file",
            )

            database.add_node(node)

            if path.parent != root:
                parent = str(path.parent)

                if parent not in database.nodes:
                    database.add_node(
                        GraphNode(
                            path=parent,
                            name=path.parent.name,
                            type="directory",
                        )
                    )

                database.add_edge(
                    GraphEdge(
                        source=parent,
                        target=str(path),
                    )
                )

        return len(database.nodes), len(database.edges)

indexer = GraphIndexer()
