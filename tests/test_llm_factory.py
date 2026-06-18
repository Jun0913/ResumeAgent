import pytest

from app.core.config import Settings
from app.services.llm.factory import create_resume_llm_client
from app.services.llm.mock import MockResumeLLMClient
from app.services.llm.openai import OpenAIResumeLLMClient


def test_factory_returns_mock_client_by_default() -> None:
    settings = Settings()

    client = create_resume_llm_client(settings)

    assert isinstance(client, MockResumeLLMClient)


def test_factory_requires_api_key_for_openai_provider() -> None:
    settings = Settings(llm_provider="openai", llm_api_key=None)

    with pytest.raises(ValueError, match="LLM_API_KEY must be set"):
        create_resume_llm_client(settings)


def test_factory_returns_openai_client_when_api_key_exists() -> None:
    settings = Settings(
        llm_provider="openai",
        llm_api_key="test-key",
        llm_model="gpt-test",
    )

    client = create_resume_llm_client(settings)

    assert isinstance(client, OpenAIResumeLLMClient)
