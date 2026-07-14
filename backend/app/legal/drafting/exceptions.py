class DraftingError(Exception):
    """Base drafting exception."""


class UnsupportedDocumentType(DraftingError):
    """Unsupported drafting type."""


class DraftValidationError(DraftingError):
    """Draft validation failed."""
