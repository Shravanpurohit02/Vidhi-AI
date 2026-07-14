from __future__ import annotations


class DraftingValidator:

    def validate(
        self,
        draft: str,
    ) -> bool:

        return bool(draft.strip())
