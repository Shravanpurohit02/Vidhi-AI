class ImportGraph:

    def build(self, modules):

        graph = {}

        for module in modules:
            graph[module.path] = module.imports

        return graph

imports = ImportGraph()
