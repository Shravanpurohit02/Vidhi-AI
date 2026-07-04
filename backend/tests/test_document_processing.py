from app.document_processing import (
    DocumentProcessingService,
)


def test_document_processing():

    service = DocumentProcessingService()

    result = service.process(
        document_id=1,
        text="""
Article 21 guarantees life and liberty.

(1978) 1 SCC 248

AIR 1978 SC 597
""",
    )

    assert result.status == "processed"
    assert result.document_id == 1
    assert result.indexed is True
    assert isinstance(result.summary, str)
    assert isinstance(result.entities, dict)
