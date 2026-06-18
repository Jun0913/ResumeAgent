from pydantic import BaseModel, Field


class ResumeJobCreateRequest(BaseModel):
    job_description: str = Field(..., min_length=1)
    profile: str = Field(..., min_length=1)


class ResumeJobResponse(BaseModel):
    job_id: str
    status: str
    keywords: list[str]
    review_summary: str
    final_cover_letter: str
