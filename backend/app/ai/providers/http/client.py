from __future__ import annotations

import httpx


class HTTPClient:

    def __init__(
        self,
        timeout: float = 120.0,
    ):
        self._client = httpx.AsyncClient(
            timeout=timeout,
            follow_redirects=True,
        )

    @property
    def client(self):
        return self._client

    async def close(self):
        await self._client.aclose()
