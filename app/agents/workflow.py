from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from app.agents.nodes import (
    DraftWriterAgent,
    FinalEditorAgent,
    JobAnalyzerAgent,
    MatchingAgent,
    ProfileAnalyzerAgent,
    ReviewAgent,
)
from app.agents.state import ResumeAgentState
from app.services.llm.base import ResumeLLMClient


class ResumeAgentWorkflow:
    def __init__(self, llm_client: ResumeLLMClient) -> None:
        self._graph = self._build_graph(llm_client)

    def invoke(self, state: ResumeAgentState) -> ResumeAgentState:
        return self._graph.invoke(state)

    def _build_graph(self, llm_client: ResumeLLMClient):
        job_analyzer = JobAnalyzerAgent()
        profile_analyzer = ProfileAnalyzerAgent()
        matching_agent = MatchingAgent()
        draft_writer = DraftWriterAgent()
        review_agent = ReviewAgent()
        final_editor = FinalEditorAgent(llm_client)

        builder = StateGraph(ResumeAgentState)
        builder.add_node("job_analyzer", job_analyzer.run)
        builder.add_node("profile_analyzer", profile_analyzer.run)
        builder.add_node("matching", matching_agent.run)
        builder.add_node("draft_writer", draft_writer.run)
        builder.add_node("review", review_agent.run)
        builder.add_node("final_editor", final_editor.run)
        builder.add_edge(START, "job_analyzer")
        builder.add_edge("job_analyzer", "profile_analyzer")
        builder.add_edge("profile_analyzer", "matching")
        builder.add_edge("matching", "draft_writer")
        builder.add_edge("draft_writer", "review")
        builder.add_edge("review", "final_editor")
        builder.add_edge("final_editor", END)
        return builder.compile()
