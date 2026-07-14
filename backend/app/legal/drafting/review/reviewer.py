from __future__ import annotations

from app.legal.drafting.validators.drafting_validator import (
    DraftingValidator,
)
from app.legal.drafting.validators.legal_validator import (
    LegalValidator,
)


class DraftReviewer:

    def __init__(self):
        self.validator = DraftingValidator()
        self.legal = LegalValidator()

    def review(
        self,
        draft: str,
    ) -> dict:

        return {
            "valid": self.validator.validate(draft),
            "warnings": self.legal.validate(draft),
        }
