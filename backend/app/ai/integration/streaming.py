from __future__ import annotations


class StreamingResponse:

    def stream(
        self,
        response: str,
    ):
        for line in response.splitlines():
            yield line
