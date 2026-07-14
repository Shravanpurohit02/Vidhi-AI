from app.ai.providers.openai_compatible import OpenAICompatibleProvider


class MistralProvider(OpenAICompatibleProvider):

    def __init__(self):
        super().__init__(
            name="mistral",
            api_key_env="MISTRAL_API_KEY",
            base_url_env="MISTRAL_BASE_URL",
            model_env="MISTRAL_MODEL",
            default_base_url="https://api.mistral.ai/v1",
            default_model="mistral-large-latest",
        )

    @property
    def supports_streaming(self) -> bool:
        return True
