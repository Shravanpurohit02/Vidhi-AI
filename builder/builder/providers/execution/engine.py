from builder.providers.execution.adapter import adapter
from builder.providers.execution.response import ExecutionResponse
from builder.providers.execution.normalizer import normalizer
from builder.providers.execution.endpoints import router as endpoint_router
from builder.providers.execution.payloads import builder as payload_builder
from builder.providers.execution.failover import engine as failover
from builder.providers.execution.streaming import engine as streaming

class ExecutionEngine:

    def execute(self, request):

        providers = failover.providers(adapter)

        if not providers:
            provider, client = adapter.client()
            providers = [provider]

        last_response = None

        for provider in providers:

            _, client = adapter.client(provider)

            payload = payload_builder.build(
                provider,
                request,
            )

            payload = streaming.prepare_payload(
                provider,
                payload,
                request,
            )

            response = client.post(
                endpoint_router.endpoint(
                    provider,
                    payload.get("model"),
                ),
                payload,
            )

            last_response = response

            if failover.should_retry(response):
                continue

            normalized = normalizer.normalize(
                provider,
                response,
            )

            return ExecutionResponse(
                success=normalized["success"],
                provider=provider.name,
                model=payload.get("model", provider.model),
                text=normalized["text"],
                usage=normalized["usage"],
                raw=normalized["raw"],
            )

        normalized = normalizer.normalize(
            provider,
            last_response,
        )

        return ExecutionResponse(
            success=normalized["success"],
            provider=provider.name,
            model=payload.get("model", provider.model),
            text=normalized["text"],
            usage=normalized["usage"],
            raw=normalized["raw"],
        )

engine = ExecutionEngine()
