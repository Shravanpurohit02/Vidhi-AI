class AIProviderError(Exception):
    """Base AI provider exception."""


class AuthenticationError(AIProviderError):
    """Authentication failed."""


class RateLimitError(AIProviderError):
    """Rate limit exceeded."""


class ProviderUnavailableError(AIProviderError):
    """Provider unavailable."""


class InvalidRequestError(AIProviderError):
    """Invalid request."""
