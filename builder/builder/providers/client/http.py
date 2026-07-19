import httpx


class HTTPClient:

    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout: float = 120.0,
    ):

        self.client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )

    def post(self, url: str, payload: dict):

        try:

            response = self.client.post(
                url,
                json=payload,
            )

            response.raise_for_status()

            return response

        except httpx.HTTPStatusError:
            raise

        except httpx.TimeoutException:
            raise

        except httpx.TransportError:
            raise

    def close(self):
        self.client.close()
