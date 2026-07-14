from app.ai.providers.openai_compatible import OpenAICompatibleProvider


class GroqProvider(OpenAICompatibleProvider):

    def __init__(self):
        super().__init__(
            name="groq",
            api_key_env="GROQ_API_KEY",
            base_url_env="GROQ_BASE_URL",
            model_env="GROQ_MODEL",
            default_base_url="https://api.groq.com/openai/v1",
            default_model="llama-3.3-70b-versatile",
        )

    @property
    def supports_streaming(self) -> bool:
        return True

    @property
    def supports_json_mode(self) -> bool:
        return True
