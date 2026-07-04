from pydantic import BaseModel, Field


class DraftRequest(BaseModel):
    template: str = Field(
        min_length=1,
        max_length=100,
    )

    facts: str = Field(
        min_length=5,
        max_length=20000,
    )

    relief: str = Field(
        default="",
        max_length=5000,
    )
