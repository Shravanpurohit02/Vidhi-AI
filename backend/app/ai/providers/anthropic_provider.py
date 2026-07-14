from app.ai.providers.openai_compatible import OpenAICompatibleProvider


class AnthropicProvider(OpenAICompatibleProvider):

    def __init__(self):
        super().__init__(
            name="anthropic",
            api_key_env="ANTHROPIC_API_KEY",
            base_url_env="ANTHROPIC_BASE_URL",
            model_env="ANTHROPIC_MODEL",
            default_base_url="https://api.anthropic.com/v1/",
            default_model="claude-sonnet-4",
        )

    @property
    def supports_streaming(self) -> bool:
        return True

    @property
    def supports_json_mode(self) -> bool:
        return True
