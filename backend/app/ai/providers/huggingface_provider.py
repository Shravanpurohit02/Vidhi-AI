from app.ai.providers.openai_compatible import OpenAICompatibleProvider


class HuggingFaceProvider(OpenAICompatibleProvider):

    def __init__(self):
        super().__init__(
            name="huggingface",
            api_key_env="HUGGINGFACE_API_KEY",
            base_url_env="HUGGINGFACE_BASE_URL",
            model_env="HUGGINGFACE_MODEL",
            default_base_url="https://router.huggingface.co/v1",
            default_model="bharatgenai/LegalParam",
        )

    @property
    def supports_embeddings(self) -> bool:
        return True
