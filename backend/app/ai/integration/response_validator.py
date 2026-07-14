from __future__ import annotations


class ResponseValidator:

    def validate(
        self,
        response: str,
    ) -> bool:

        return bool(response and response.strip())
