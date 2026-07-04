from pydantic import BaseModel, Field


class ReasoningRequest(BaseModel):
    text: str = Field(
        min_length=10,
        max_length=50000,
    )
