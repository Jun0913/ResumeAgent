from app.agents.workflow import ResumeAgentWorkflow
from app.services.llm.mock import MockResumeLLMClient


def test_workflow_runs_agents_in_expected_order() -> None:
    workflow = ResumeAgentWorkflow(MockResumeLLMClient())

    result = workflow.invoke(
        {
            "job_id": "job-123",
            "job_description": "Cloud infrastructure engineer with Terraform and AWS IAM",
            "profile": "Engineer with Python automation and infrastructure experience.",
            "status": "pending",
            "completed_steps": [],
        }
    )

    assert result["status"] == "completed"
    assert result["completed_steps"] == [
        "JobAnalyzerAgent",
        "ProfileAnalyzerAgent",
        "MatchingAgent",
        "DraftWriterAgent",
        "ReviewAgent",
        "FinalEditorAgent",
    ]
    assert result["keywords"]
    assert result["review_summary"]
    assert "mock cover letter" in result["final_cover_letter"].lower()
