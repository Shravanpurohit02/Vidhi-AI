from __future__ import annotations

from time import perf_counter

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import get_logger

logger = get_logger()


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        started = perf_counter()

        response = await call_next(request)

        elapsed = perf_counter() - started

        request_id = getattr(
            request.state,
            "request_id",
            "-",
        )

        logger.info(
            "%s %s -> %s (%.3fs) [request_id=%s]",
            request.method,
            request.url.path,
            response.status_code,
            elapsed,
            request_id,
        )

        return response
