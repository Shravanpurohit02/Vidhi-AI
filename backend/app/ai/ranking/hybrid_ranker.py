class HybridRanker:

    def combine(
        self,
        lexical,
        semantic,
    ):

        merged = []

        seen = set()

        for result in lexical + semantic:

            text = result.get("text", "")

            if text in seen:
                continue

            seen.add(text)

            merged.append(result)

        return merged
