from functools import lru_cache

from app.agents.workflow import ResumeAgentWorkflow
from app.core.config import get_settings
from app.db.repositories import ResumeJobRepository
from app.db.sqlite import SQLiteDatabase
from app.services.llm.factory import create_resume_llm_client
from app.services.output_writer import OutputWriter
from app.services.resume_jobs import ResumeJobService


@lru_cache
def get_resume_job_service() -> ResumeJobService:
    settings = get_settings()
    database = SQLiteDatabase(settings.database_path)
    repository = ResumeJobRepository(database)
    output_writer = OutputWriter(settings.outputs_dir)
    llm_client = create_resume_llm_client(settings)
    workflow = ResumeAgentWorkflow(llm_client)
    return ResumeJobService(
        repository=repository,
        output_writer=output_writer,
        workflow=workflow,
    )
