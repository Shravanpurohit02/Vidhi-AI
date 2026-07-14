from builder.providers.execution.adapter import adapter
from builder.providers.execution.response import ExecutionResponse

class ExecutionEngine:

    def execute(self, request):

        provider, client = adapter.client()

        payload = {
            "model": request.model or provider.model,
            "messages": [
                {
                    "role": m.role,
                    "content": m.content,
                }
                for m in request.messages
            ],
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
            "stream": request.stream,
        }

        response = client.post(
            "/chat/completions",
            payload,
        )

        return ExecutionResponse(
            success=response.is_success,
            provider=provider.name,
            model=payload["model"],
            text=response.text,
            usage={},
            raw=response.json() if response.content else {},
        )

engine = ExecutionEngine()
