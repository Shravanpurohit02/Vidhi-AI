class ReverseReferenceIndex:

    def build(self, repository):

        reverse = {}

        for symbol, refs in repository.references.items():

            for ref in refs:

                module = ref.get("module")
                if not module:
                    continue

                reverse.setdefault(module, set()).add(symbol)

        return {
            module: sorted(symbols)
            for module, symbols in reverse.items()
        }


reverse_index = ReverseReferenceIndex()
