from app.core.config import Settings
from app.services.llm.base import ResumeLLMClient
from app.services.llm.mock import MockResumeLLMClient
from app.services.llm.openai import OpenAIResumeLLMClient


def create_resume_llm_client(settings: Settings) -> ResumeLLMClient:
    provider = settings.llm_provider.lower()

    if provider == "mock":
        return MockResumeLLMClient()

    if provider == "openai":
        if not settings.llm_api_key:
            raise ValueError("LLM_API_KEY must be set when LLM_PROVIDER=openai")
        return OpenAIResumeLLMClient(
            api_key=settings.llm_api_key,
            model=settings.llm_model,
        )

    raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
