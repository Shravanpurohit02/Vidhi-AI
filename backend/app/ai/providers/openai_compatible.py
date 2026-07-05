import os

from openai import OpenAI

from app.ai.interfaces.base_provider import BaseAIProvider


class OpenAICompatibleProvider(BaseAIProvider):

    def __init__(
        self,
        name: str,
        api_key_env: str,
        base_url_env: str,
        model_env: str,
        default_base_url: str,
        default_model: str,
    ):
        self._name = name

        self.api_key = os.getenv(
            api_key_env,
            "",
        )

        self.base_url = os.getenv(
            base_url_env,
            default_base_url,
        )

        self._model = os.getenv(
            model_env,
            default_model,
        )

    @property
    def name(self):
        return self._name

    @property
    def model(self):
        return self._model

    def health(self):
        return bool(self.api_key)

    def _client(self):

        if not self.api_key:
            raise RuntimeError(f"{self._name} API key not configured.")

        return OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:

        client = self._client()

        messages = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        response = client.chat.completions.create(
            model=self._model,
            messages=messages,
            temperature=0.2,
        )

        return response.choices[0].message.content
