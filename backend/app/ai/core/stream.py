from app.ai.integration.streaming import StreamingResponse

# Legacy compatibility aliases
StreamingResponse = StreamingResponse

StreamProvider = StreamingResponse
StreamManager = StreamingResponse
StreamResponse = StreamingResponse
Stream = StreamingResponse
AIStream = StreamingResponse

stream = StreamingResponse

__all__ = [
    "StreamingResponse",
    "StreamProvider",
    "StreamManager",
    "StreamResponse",
    "Stream",
    "AIStream",
    "stream",
]
