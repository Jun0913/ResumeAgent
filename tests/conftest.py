from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.core.config import get_settings
from app.dependencies import get_resume_job_service
from app.main import create_app


@pytest.fixture
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> TestClient:
    database_path = tmp_path / "resume_agent.db"
    outputs_dir = tmp_path / "outputs"

    monkeypatch.setenv("DATABASE_PATH", str(database_path))
    monkeypatch.setenv("OUTPUTS_DIR", str(outputs_dir))

    get_settings.cache_clear()
    get_resume_job_service.cache_clear()

    app = create_app()

    with TestClient(app) as test_client:
        yield test_client

    get_resume_job_service.cache_clear()
    get_settings.cache_clear()
