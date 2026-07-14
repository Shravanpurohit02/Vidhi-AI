from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider


def configure_tracing(app):
    provider = TracerProvider(
        resource=Resource.create(
            {
                "service.name": "vidhi-ai",
                "service.version": "0.1.0",
            }
        )
    )

    trace.set_tracer_provider(provider)

    FastAPIInstrumentor.instrument_app(app)
