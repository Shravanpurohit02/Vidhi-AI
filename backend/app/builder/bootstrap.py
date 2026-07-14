from typing import Any

from .context import create_context
from .dispatcher import dispatcher, BuilderRequest


def boot_builder(
    operation: str = "inspect",
    workspace: str | None = None,
    payload: dict[str, Any] | None = None,
):
    """
    Bootstrap the embedded Builder runtime.
    """

    ctx = create_context()

    request = BuilderRequest(
        operation=operation,
        workspace=workspace or ctx.workspace,
        payload=payload,
    )

    return dispatcher.dispatch(request)
