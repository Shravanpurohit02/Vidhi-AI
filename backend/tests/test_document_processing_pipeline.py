from pathlib import Path

from app.tasks.document_tasks import DocumentTasks


class DummyDocument:

    id = 1

    file_path = "storage/documents/test.txt"


def test_processing_pipeline():

    Path("storage/documents").mkdir(
        parents=True,
        exist_ok=True,
    )

    Path("storage/documents/test.txt").write_text("Article 21 protects life.")

    result = DocumentTasks.process_uploaded_document(
        DummyDocument(),
    )

    assert result.status == "processed"


class MissingDocument:

    id = 999

    file_path = "storage/documents/does_not_exist.txt"


def test_missing_document_pipeline():

    result = DocumentTasks.process_uploaded_document(
        MissingDocument(),
    )

    assert result["status"] == "missing_file"
