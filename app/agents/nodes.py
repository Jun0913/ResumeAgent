from __future__ import annotations

from app.agents.state import ResumeAgentState
from app.services.llm.base import ResumeLLMClient


class JobAnalyzerAgent:
    def run(self, state: ResumeAgentState) -> dict[str, object]:
        normalized = state["job_description"].replace(",", " ").replace(".", " ").split()
        keywords: list[str] = []

        for word in normalized:
            token = word.strip().lower()
            if len(token) < 4:
                continue
            if token in keywords:
                continue
            keywords.append(token)
            if len(keywords) == 5:
                break

        if not keywords:
            keywords = ["mock", "resume", "agent"]

        return {
            "keywords": keywords,
            "completed_steps": ["JobAnalyzerAgent"],
        }


class ProfileAnalyzerAgent:
    def run(self, state: ResumeAgentState) -> dict[str, object]:
        profile_text = state["profile"].strip()
        sentences = [sentence.strip() for sentence in profile_text.split(".") if sentence.strip()]
        profile_summary = sentences[0] if sentences else profile_text

        return {
            "profile_summary": profile_summary,
            "completed_steps": ["ProfileAnalyzerAgent"],
        }


class MatchingAgent:
    def run(self, state: ResumeAgentState) -> dict[str, object]:
        keywords = ", ".join(state["keywords"])
        matching_summary = (
            f"Candidate experience aligns with the target role through key areas: {keywords}. "
            f"Profile summary: {state['profile_summary']}."
        )
        return {
            "matching_summary": matching_summary,
            "completed_steps": ["MatchingAgent"],
        }


class DraftWriterAgent:
    def run(self, state: ResumeAgentState) -> dict[str, object]:
        draft_cover_letter = (
            "Draft cover letter for review. "
            f"Target role focus: {state['matching_summary']} "
            f"Candidate background: {state['profile_summary']}."
        )
        return {
            "draft_cover_letter": draft_cover_letter,
            "completed_steps": ["DraftWriterAgent"],
        }


class ReviewAgent:
    def run(self, state: ResumeAgentState) -> dict[str, object]:
        review_summary = (
            "Mock review completed. The draft aligns the profile with the role and is ready for final editing."
        )
        return {
            "review_summary": review_summary,
            "completed_steps": ["ReviewAgent"],
        }


class FinalEditorAgent:
    def __init__(self, llm_client: ResumeLLMClient) -> None:
        self._llm_client = llm_client

    def run(self, state: ResumeAgentState) -> dict[str, object]:
        llm_result = self._llm_client.generate_resume_artifacts(
            profile=state["profile"],
            job_description=state["job_description"],
        )
        final_cover_letter = (
            f"{llm_result.final_cover_letter} "
            f"Review summary: {state['review_summary']}"
        )

        return {
            "final_cover_letter": final_cover_letter,
            "status": "completed",
            "completed_steps": ["FinalEditorAgent"],
        }
