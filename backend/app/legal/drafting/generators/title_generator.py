from __future__ import annotations


class TitleGenerator:

    def generate(
        self,
        document_type: str,
    ) -> str:

        return f"Draft {document_type.title()}"
