from __future__ import annotations

import operator
from typing import Annotated, TypedDict


class ResumeAgentState(TypedDict, total=False):
    job_id: str
    job_description: str
    profile: str
    keywords: list[str]
    profile_summary: str
    matching_summary: str
    draft_cover_letter: str
    review_summary: str
    final_cover_letter: str
    status: str
    completed_steps: Annotated[list[str], operator.add]
