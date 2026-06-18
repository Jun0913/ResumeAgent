from __future__ import annotations

import json

from app.db.models import ResumeJobRecord
from app.db.sqlite import SQLiteDatabase


class ResumeJobRepository:
    def __init__(self, database: SQLiteDatabase) -> None:
        self._database = database
        self.initialize()

    def initialize(self) -> None:
        with self._database.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS resume_jobs (
                    job_id TEXT PRIMARY KEY,
                    job_description TEXT NOT NULL,
                    profile TEXT NOT NULL,
                    status TEXT NOT NULL,
                    keywords TEXT NOT NULL,
                    review_summary TEXT NOT NULL,
                    final_cover_letter TEXT NOT NULL
                )
                """
            )
            connection.commit()

    def save(self, job: ResumeJobRecord) -> None:
        with self._database.connect() as connection:
            connection.execute(
                """
                INSERT INTO resume_jobs (
                    job_id,
                    job_description,
                    profile,
                    status,
                    keywords,
                    review_summary,
                    final_cover_letter
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    job.job_id,
                    job.job_description,
                    job.profile,
                    job.status,
                    json.dumps(job.keywords),
                    job.review_summary,
                    job.final_cover_letter,
                ),
            )
            connection.commit()

    def get(self, job_id: str) -> ResumeJobRecord | None:
        with self._database.connect() as connection:
            row = connection.execute(
                """
                SELECT
                    job_id,
                    job_description,
                    profile,
                    status,
                    keywords,
                    review_summary,
                    final_cover_letter
                FROM resume_jobs
                WHERE job_id = ?
                """,
                (job_id,),
            ).fetchone()

        if row is None:
            return None

        return ResumeJobRecord(
            job_id=row["job_id"],
            job_description=row["job_description"],
            profile=row["profile"],
            status=row["status"],
            keywords=json.loads(row["keywords"]),
            review_summary=row["review_summary"],
            final_cover_letter=row["final_cover_letter"],
        )
