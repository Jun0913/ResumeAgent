import json
import sqlite3
from pathlib import Path

from fastapi.testclient import TestClient


def test_create_resume_job_returns_mock_result(client: TestClient) -> None:
    response = client.post(
        "/api/v1/resume-jobs",
        json={
            "job_description": "Cloud infrastructure engineer with Terraform, AWS IAM, and Python automation",
            "profile": "Backend engineer experienced in Python services and infrastructure automation",
        },
    )

    body = response.json()

    assert response.status_code == 201
    assert body["job_id"]
    assert body["status"] == "completed"
    assert "terraform" in body["keywords"]
    assert body["review_summary"]
    assert "mock cover letter" in body["final_cover_letter"].lower()


def test_get_resume_job_returns_created_job(client: TestClient) -> None:
    create_response = client.post(
        "/api/v1/resume-jobs",
        json={
            "job_description": "Platform engineer focused on AWS IAM and CI automation",
            "profile": "Engineer with CI/CD and cloud governance experience",
        },
    )
    job_id = create_response.json()["job_id"]

    response = client.get(f"/api/v1/resume-jobs/{job_id}")

    assert response.status_code == 200
    assert response.json()["job_id"] == job_id


def test_get_resume_job_returns_404_for_missing_job(client: TestClient) -> None:
    response = client.get("/api/v1/resume-jobs/missing-job-id")

    assert response.status_code == 404
    assert response.json() == {"detail": "Resume job not found"}


def test_create_resume_job_persists_sqlite_and_output_files(
    client: TestClient,
    tmp_path: Path,
) -> None:
    response = client.post(
        "/api/v1/resume-jobs",
        json={
            "job_description": "Infrastructure engineer with Python, Terraform, and IAM policy design",
            "profile": "Engineer building internal platforms and automation services",
        },
    )
    body = response.json()
    job_id = body["job_id"]

    database_path = tmp_path / "resume_agent.db"
    outputs_dir = tmp_path / "outputs"
    json_path = outputs_dir / f"{job_id}.json"
    markdown_path = outputs_dir / f"{job_id}.md"

    assert json_path.exists()
    assert markdown_path.exists()

    saved_payload = json.loads(json_path.read_text(encoding="utf-8"))
    assert saved_payload["job_id"] == job_id
    assert saved_payload["status"] == "completed"

    markdown_body = markdown_path.read_text(encoding="utf-8")
    assert job_id in markdown_body
    assert "Final Cover Letter" in markdown_body

    with sqlite3.connect(database_path) as connection:
        row = connection.execute(
            "SELECT job_id, status FROM resume_jobs WHERE job_id = ?",
            (job_id,),
        ).fetchone()

    assert row == (job_id, "completed")
