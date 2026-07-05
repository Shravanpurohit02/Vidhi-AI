from app.legal.research.pipeline.research_pipeline import (
    ResearchPipeline,
)


def test_pipeline():

    pipeline = ResearchPipeline()

    result = pipeline.execute("Explain consideration in contract law.")

    assert "answer" in result
    assert "citations" in result
