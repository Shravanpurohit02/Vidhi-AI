class EvidenceError(Exception):
    """Base evidence exception."""


class EvidenceNotFound(EvidenceError):
    """Evidence not found."""


class IntegrityCheckFailed(EvidenceError):
    """Integrity verification failed."""


class StorageProviderError(EvidenceError):
    """Storage provider error."""
