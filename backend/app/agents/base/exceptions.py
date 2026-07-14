from __future__ import annotations


class AgentError(Exception):
    """Base agent exception."""


class AgentRegistrationError(AgentError):
    """Raised when an agent cannot be registered."""


class AgentNotFoundError(AgentError):
    """Raised when an agent cannot be located."""


class AgentExecutionError(AgentError):
    """Raised when an agent execution fails."""


class AgentValidationError(AgentError):
    """Raised when an agent request is invalid."""
