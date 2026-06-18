from __future__ import annotations

import json
from pathlib import Path

from app.db.models import ResumeJobRecord


class OutputWriter:
    def __init__(self, outputs_dir: str) -> None:
        self._outputs_dir = Path(outputs_dir)
        self._outputs_dir.mkdir(parents=True, exist_ok=True)

    def write(self, job: ResumeJobRecord) -> None:
        payload = {
            "job_id": job.job_id,
            "status": job.status,
            "keywords": job.keywords,
            "review_summary": job.review_summary,
            "final_cover_letter": job.final_cover_letter,
            "job_description": job.job_description,
            "profile": job.profile,
        }

        json_path = self._outputs_dir / f"{job.job_id}.json"
        markdown_path = self._outputs_dir / f"{job.job_id}.md"

        json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        markdown_path.write_text(self._build_markdown(job), encoding="utf-8")

    def _build_markdown(self, job: ResumeJobRecord) -> str:
        keywords = ", ".join(job.keywords)

        return (
            f"# Resume Job {job.job_id}\n\n"
            f"## Status\n{job.status}\n\n"
            f"## Keywords\n{keywords}\n\n"
            f"## Review Summary\n{job.review_summary}\n\n"
            f"## Final Cover Letter\n{job.final_cover_letter}\n"
        )
