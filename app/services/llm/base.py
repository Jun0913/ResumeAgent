from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class ResumeGenerationResult:
    keywords: list[str]
    review_summary: str
    final_cover_letter: str


class ResumeLLMClient(Protocol):
    def generate_resume_artifacts(
        self,
        *,
        profile: str,
        job_description: str,
    ) -> ResumeGenerationResult: ...
