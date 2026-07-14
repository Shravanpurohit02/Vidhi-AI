from app.ai.providers.openai_compatible import OpenAICompatibleProvider


class OpenRouterProvider(OpenAICompatibleProvider):

    def __init__(self):
        super().__init__(
            name="openrouter",
            api_key_env="OPENROUTER_API_KEY",
            base_url_env="OPENROUTER_BASE_URL",
            model_env="OPENROUTER_MODEL",
            default_base_url="https://openrouter.ai/api/v1",
            default_model="deepseek/deepseek-r1",
        )

    @property
    def supports_streaming(self) -> bool:
        return True

    @property
    def supports_json_mode(self) -> bool:
        return True
