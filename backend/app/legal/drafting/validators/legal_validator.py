from __future__ import annotations


class LegalValidator:

    def validate(
        self,
        draft: str,
    ) -> list[str]:

        warnings: list[str] = []

        if len(draft) < 500:
            warnings.append("Draft appears unusually short.")

        return warnings
