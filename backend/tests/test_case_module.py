from pathlib import Path

import pytest

REQUIRED_FILES = [
    "app/models/case.py",
    "app/schemas/case.py",
    "app/repositories/case_repository.py",
    "app/services/case_service.py",
    "app/api/v1/cases.py",
]


def test_case_module_structure():
    for file in REQUIRED_FILES:
        assert Path(file).exists(), f"{file} missing"


@pytest.mark.parametrize(
    "endpoint",
    [
        "/cases",
        "/cases/search?q=test",
        "/cases/statistics",
        "/cases/status/Draft",
    ],
)
def test_case_endpoints_exist(endpoint):
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    response = client.get(endpoint)

    assert response.status_code in (200, 307, 401)
