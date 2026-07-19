from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class ProviderCatalogEntry:
    name: str
    display_name: str
    env_prefix: str
    api_type: str

    default_model: str = ""
    default_base_url: str = ""

    free_tier: bool = False

    supports_streaming: bool = True
    supports_tools: bool = False
    supports_vision: bool = False
    supports_reasoning: bool = False
    supports_embeddings: bool = False

    context_window: int = 0
    max_output_tokens: int = 0

    priority: int = 100

    aliases: tuple[str, ...] = field(default_factory=tuple)


PROVIDERS: tuple[ProviderCatalogEntry, ...] = (

    ProviderCatalogEntry(
        name="groq",
        display_name="Groq",
        env_prefix="GROQ",
        api_type="openai_compatible",
        free_tier=True,
        supports_streaming=True,
        supports_tools=True,
        supports_reasoning=True,
        priority=10,
        aliases=("groq",),
    ),

    ProviderCatalogEntry(
        name="gemini",
        display_name="Google Gemini",
        env_prefix="GOOGLE",
        api_type="native",
        free_tier=True,
        supports_streaming=True,
        supports_tools=True,
        supports_vision=True,
        supports_reasoning=True,
        priority=20,
        aliases=("gemini", "google"),
    ),

    ProviderCatalogEntry(
        name="openrouter",
        display_name="OpenRouter",
        env_prefix="OPENROUTER",
        api_type="openai_compatible",
        free_tier=True,
        supports_streaming=True,
        supports_tools=True,
        supports_reasoning=True,
        priority=30,
        aliases=("openrouter",),
    ),

    ProviderCatalogEntry(
        name="cerebras",
        display_name="Cerebras",
        env_prefix="CEREBRAS",
        api_type="openai_compatible",
        free_tier=True,
        supports_streaming=True,
        supports_reasoning=True,
        priority=40,
        aliases=("cerebras",),
    ),

    ProviderCatalogEntry(
        name="nvidia",
        display_name="NVIDIA NIM",
        env_prefix="NVIDIA",
        api_type="openai_compatible",
        supports_streaming=True,
        supports_reasoning=True,
        priority=50,
        aliases=("nvidia",),
    ),

    ProviderCatalogEntry(
        name="mistral",
        display_name="Mistral",
        env_prefix="MISTRAL",
        api_type="native",
        supports_streaming=True,
        supports_reasoning=True,
        priority=60,
        aliases=("mistral",),
    ),

    ProviderCatalogEntry(
        name="anthropic",
        display_name="Anthropic",
        env_prefix="ANTHROPIC",
        api_type="native",
        supports_streaming=True,
        supports_tools=True,
        supports_vision=True,
        supports_reasoning=True,
        priority=70,
        aliases=("anthropic", "claude"),
    ),

    ProviderCatalogEntry(
        name="openai",
        display_name="OpenAI",
        env_prefix="OPENAI",
        api_type="native",
        supports_streaming=True,
        supports_tools=True,
        supports_vision=True,
        supports_reasoning=True,
        priority=80,
        aliases=("openai", "chatgpt"),
    ),

    ProviderCatalogEntry(
        name="huggingface",
        display_name="Hugging Face",
        env_prefix="HUGGINGFACE",
        api_type="native",
        supports_reasoning=False,
        priority=90,
        aliases=("huggingface", "hf"),
    ),
)
