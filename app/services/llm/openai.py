from app.services.llm.base import ResumeGenerationResult


class OpenAIResumeLLMClient:
    def __init__(self, api_key: str, model: str) -> None:
        self._api_key = api_key
        self._model = model

    def generate_resume_artifacts(
        self,
        *,
        profile: str,
        job_description: str,
    ) -> ResumeGenerationResult:
        raise NotImplementedError(
            "OpenAI client integration is not implemented yet. "
            "Set LLM_PROVIDER=mock for local development."
        )
