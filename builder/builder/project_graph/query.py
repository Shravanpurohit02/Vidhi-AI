from builder.project_graph.database import database

class GraphQuery:

    def node(self, path: str):
        return database.nodes.get(path)

    def children(self, path: str):
        return [
            e.target
            for e in database.edges
            if e.source == path
        ]

query = GraphQuery()
