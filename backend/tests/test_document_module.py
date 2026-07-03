from pathlib import Path


def test_storage_directory_exists():
    assert Path("storage/documents").exists()


def test_document_module_files():
    assert Path("app/utils/file_storage.py").exists()
    assert Path("app/api/v1/documents.py").exists()
