from __future__ import annotations

from uuid import uuid4

from app.agents.workflow import ResumeAgentWorkflow
from app.api.schemas.resume_jobs import ResumeJobCreateRequest, ResumeJobResponse
from app.db.models import ResumeJobRecord
from app.db.repositories import ResumeJobRepository
from app.services.output_writer import OutputWriter


class ResumeJobService:
    def __init__(
        self,
        repository: ResumeJobRepository,
        output_writer: OutputWriter,
        workflow: ResumeAgentWorkflow,
    ) -> None:
        self._repository = repository
        self._output_writer = output_writer
        self._workflow = workflow

    def create_job(self, payload: ResumeJobCreateRequest) -> ResumeJobResponse:
        job_id = str(uuid4())
        workflow_result = self._workflow.invoke(
            {
                "job_id": job_id,
                "job_description": payload.job_description,
                "profile": payload.profile,
                "status": "pending",
                "completed_steps": [],
            }
        )

        job = ResumeJobRecord(
            job_id=job_id,
            job_description=payload.job_description,
            profile=payload.profile,
            status=workflow_result["status"],
            keywords=workflow_result["keywords"],
            review_summary=workflow_result["review_summary"],
            final_cover_letter=workflow_result["final_cover_letter"],
        )
        self._repository.save(job)
        self._output_writer.write(job)
        return self._to_response(job)

    def get_job(self, job_id: str) -> ResumeJobResponse | None:
        job = self._repository.get(job_id)
        if job is None:
            return None
        return self._to_response(job)

    def _to_response(self, job: ResumeJobRecord) -> ResumeJobResponse:
        return ResumeJobResponse(
            job_id=job.job_id,
            status=job.status,
            keywords=job.keywords,
            review_summary=job.review_summary,
            final_cover_letter=job.final_cover_letter,
        )
