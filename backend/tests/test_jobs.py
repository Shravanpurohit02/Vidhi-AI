from fastapi.testclient import TestClient

from app.main import app
from app.tasks.document_tasks import enqueue_document_index

client = TestClient(app)


def test_job_queue():

    enqueue_document_index(1)

    response = client.get("/jobs/status")

    assert response.status_code == 200

    assert response.json()["queued_jobs"] >= 1
