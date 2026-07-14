from builder.project_graph.node import GraphNode
from builder.project_graph.edge import GraphEdge

class GraphDatabase:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node: GraphNode):
        self.nodes[node.path] = node

    def add_edge(self, edge: GraphEdge):
        self.edges.append(edge)

database = GraphDatabase()
