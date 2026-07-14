from app.ai.providers.openai_compatible import OpenAICompatibleProvider


class CerebrasProvider(OpenAICompatibleProvider):

    def __init__(self):
        super().__init__(
            name="cerebras",
            api_key_env="CEREBRAS_API_KEY",
            base_url_env="CEREBRAS_BASE_URL",
            model_env="CEREBRAS_MODEL",
            default_base_url="https://api.cerebras.ai/v1",
            default_model="llama-4-scout-17b-16e-instruct",
        )

    @property
    def supports_streaming(self) -> bool:
        return True
