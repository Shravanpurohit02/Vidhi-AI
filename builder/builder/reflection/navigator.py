class SemanticNavigator:

    def module(self, repository, module: str):
        return repository.modules.get(module)

    def symbol(self, repository, symbol: str):
        return [
            s
            for s in repository.symbols.values()
            if s.name == symbol
        ]

    def references(self, repository, symbol: str):
        return repository.references.get(symbol, [])

    def callees(self, repository, module: str):
        return repository.call_graph.get(module, [])

    def callers(self, repository, module: str):

        callers = []

        for caller_module, edges in repository.call_graph.items():

            for edge in edges:

                if edge.callee == module:
                    callers.append(edge)

        return callers


navigator = SemanticNavigator()
