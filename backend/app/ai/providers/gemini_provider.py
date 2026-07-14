from app.ai.providers.openai_compatible import OpenAICompatibleProvider


class GeminiProvider(OpenAICompatibleProvider):

    def __init__(self):
        super().__init__(
            name="gemini",
            api_key_env="GEMINI_API_KEY",
            base_url_env="GEMINI_BASE_URL",
            model_env="GEMINI_MODEL",
            default_base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            default_model="gemini-2.5-pro",
        )

    @property
    def supports_streaming(self) -> bool:
        return True

    @property
    def supports_json_mode(self) -> bool:
        return True
