from __future__ import annotations

import time

from app.verification.registry import VerificationRegistry
from app.verification.checks import (
    CompileCheck,
    ImportCheck,
    ModelCheck,
    AlembicCheck,
    RouteCheck,
    ConfigurationCheck,
    ServiceCheck,
    RepositoryCheck,
    RAGPipelineCheck,
    RetrieverCheck,
    VectorIndexCheck,
    EmbeddingProviderCheck,
    DocumentProcessingCheck,
    DatabaseConnectionCheck,
    SecurityCheck,
    PerformanceCheck,
    EndToEndCheck,
)


class VerificationEngine:

    def __init__(self):

        self.registry = VerificationRegistry()

        self.registry.register(CompileCheck())
        self.registry.register(ImportCheck())
        self.registry.register(ModelCheck())
        self.registry.register(AlembicCheck())
        self.registry.register(RouteCheck())
        self.registry.register(ConfigurationCheck())
        self.registry.register(ServiceCheck())
        self.registry.register(RepositoryCheck())
        self.registry.register(RAGPipelineCheck())
        self.registry.register(RetrieverCheck())
        self.registry.register(VectorIndexCheck())
        self.registry.register(EmbeddingProviderCheck())
        self.registry.register(DocumentProcessingCheck())
        self.registry.register(DatabaseConnectionCheck())
        self.registry.register(SecurityCheck())
        self.registry.register(PerformanceCheck())
        self.registry.register(EndToEndCheck())

    def register(self, check):
        self.registry.register(check)

    def run(self):

        results = []

        for check in self.registry.checks():

            started = time.perf_counter()

            result = check.run()

            result.duration = time.perf_counter() - started

            results.append(result)

        return results
