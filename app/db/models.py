from dataclasses import dataclass


@dataclass
class ResumeJobRecord:
    job_id: str
    job_description: str
    profile: str
    status: str
    keywords: list[str]
    review_summary: str
    final_cover_letter: str
