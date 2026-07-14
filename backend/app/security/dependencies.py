from __future__ import annotations

from fastapi import HTTPException, Request, status

from app.security.rate_limit import limiter


def rate_limit(
    limit: int = 60,
    window_seconds: int = 60,
):
    async def dependency(request: Request):
        ip = request.client.host if request.client else "unknown"

        if not limiter.allow(
            ip,
            limit,
            window_seconds,
        ):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded",
            )

    return dependency
