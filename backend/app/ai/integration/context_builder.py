from __future__ import annotations


class ContextBuilder:

    def build(
        self,
        documents: list[str],
    ) -> str:

        return "\n\n".join(documents)
