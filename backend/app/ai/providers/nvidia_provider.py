from app.ai.providers.openai_compatible import OpenAICompatibleProvider


class NVIDIAProvider(OpenAICompatibleProvider):

    def __init__(self):
        super().__init__(
            name="nvidia",
            api_key_env="NVIDIA_API_KEY",
            base_url_env="NVIDIA_BASE_URL",
            model_env="NVIDIA_MODEL",
            default_base_url="https://integrate.api.nvidia.com/v1",
            default_model="nvidia/llama-3.3-nemotron-super-49b-v1",
        )

    @property
    def supports_streaming(self) -> bool:
        return True

    @property
    def supports_embeddings(self) -> bool:
        return True

    @property
    def supports_json_mode(self) -> bool:
        return True
