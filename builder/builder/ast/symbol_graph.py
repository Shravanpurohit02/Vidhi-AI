class SymbolGraph:

    def build(self, modules):

        definitions = {}
        references = {}
        exports = {}
        duplicates = {}

        for module in modules:

            path = module.path

            exports[path] = list(module.exports)

            references[path] = sorted(
                set(
                    module.imports
                    + module.classes
                    + module.functions
                    + module.async_functions
                )
            )

            for symbol in (
                module.classes
                + module.functions
                + module.async_functions
            ):

                definitions.setdefault(
                    symbol,
                    [],
                ).append(path)

        for symbol, files in definitions.items():

            if len(files) > 1:
                duplicates[symbol] = sorted(files)

        return {
            "definitions": definitions,
            "references": references,
            "exports": exports,
            "duplicates": duplicates,
        }

    def find_definition(
        self,
        graph,
        symbol,
    ):

        return graph["definitions"].get(
            symbol,
            [],
        )

    def find_references(
        self,
        graph,
        path,
    ):

        return graph["references"].get(
            path,
            [])


graph = SymbolGraph()
