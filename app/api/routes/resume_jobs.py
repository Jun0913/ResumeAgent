from fastapi import APIRouter, Depends, HTTPException, status

from app.api.schemas.resume_jobs import ResumeJobCreateRequest, ResumeJobResponse
from app.dependencies import get_resume_job_service
from app.services.resume_jobs import ResumeJobService

router = APIRouter(prefix="/api/v1/resume-jobs", tags=["resume-jobs"])


@router.post("", response_model=ResumeJobResponse, status_code=status.HTTP_201_CREATED)
def create_resume_job(
    payload: ResumeJobCreateRequest,
    service: ResumeJobService = Depends(get_resume_job_service),
) -> ResumeJobResponse:
    return service.create_job(payload)


@router.get("/{job_id}", response_model=ResumeJobResponse)
def get_resume_job(
    job_id: str,
    service: ResumeJobService = Depends(get_resume_job_service),
) -> ResumeJobResponse:
    job = service.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resume job not found")
    return job
