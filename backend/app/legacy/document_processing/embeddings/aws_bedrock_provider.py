from __future__ import annotations
import importlib.util
from app.document_processing.embeddings.provider import EmbeddingProvider


class AWSBedrockProvider(EmbeddingProvider):
    @property
    def name(self):
        return "aws_bedrock"

    @property
    def dimensions(self):
        return 1024

    @property
    def supports_batch(self):
        return True

    def is_available(self):
        return importlib.util.find_spec("boto3") is not None

    def embed(self, text: str):
        raise NotImplementedError("AWS Bedrock embedding pending.")
