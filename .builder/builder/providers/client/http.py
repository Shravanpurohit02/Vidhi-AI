import httpx

class HTTPClient:

    def __init__(self, base_url: str, api_key: str):
        self.client = httpx.Client(
            base_url=base_url,
            timeout=120.0,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )

    def post(self, url: str, payload: dict):
        return self.client.post(url, json=payload)
