# Resume Agent Platform

Resume Agent Platform is a local-first portfolio project for a cloud and infrastructure engineer. It exposes a FastAPI API, runs a LangGraph-based multi-agent workflow in `mock` mode by default, stores job metadata in SQLite, and writes outputs to local JSON and Markdown files.

## Overview

- FastAPI API server
- LangGraph workflow with six agents
- SQLite persistence
- Local `outputs/` storage
- Docker Compose local runtime
- Terraform limited to AWS IAM resources only
- GitHub Actions for validation only

## Current API

- `GET /health`
- `POST /api/v1/resume-jobs`
- `GET /api/v1/resume-jobs/{job_id}`

## Workflow

```text
JobAnalyzerAgent
-> ProfileAnalyzerAgent
-> MatchingAgent
-> DraftWriterAgent
-> ReviewAgent
-> FinalEditorAgent
```

Final response fields:

- `job_id`
- `status`
- `keywords`
- `review_summary`
- `final_cover_letter`

## Project Structure

```text
app/
  agents/
  api/
  core/
  db/
  services/
tests/
terraform/
.github/workflows/
data/
outputs/
```

## Environment Variables

```env
APP_NAME=Resume Agent Platform
APP_ENV=local
APP_HOST=0.0.0.0
APP_PORT=8000
LLM_PROVIDER=mock
LLM_API_KEY=
LLM_MODEL=mock-resume-agent
DATABASE_PATH=data/resume_agent.db
OUTPUTS_DIR=outputs
```

## Local Development

### Run with venv

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs`.

### Run checks

```powershell
.\.venv\Scripts\Activate.ps1
ruff check .
pytest
```

## Docker Compose

```bash
docker compose up --build
docker compose down
```

Volumes:

- `./data:/app/data`
- `./outputs:/app/outputs`

## LLM Provider Policy

- Default provider is `mock`
- No real LLM API call is made in `mock` mode
- Real LLM integration is only allowed when the user explicitly provides an API key and changes the provider
- The current `openai` client is a guarded placeholder and does not call the API yet

## Storage

- SQLite database: `data/resume_agent.db`
- JSON outputs: `outputs/{job_id}.json`
- Markdown outputs: `outputs/{job_id}.md`

## Terraform Scope

Allowed resources:

- IAM User
- IAM Group
- IAM Policy
- IAM Role
- IAM Policy Attachment
- GitHub Actions OIDC Provider
- GitHub Actions Assume Role

Forbidden resources:

- EC2
- ECS
- ECR
- S3
- RDS
- DynamoDB
- SQS
- Lambda
- ALB
- NAT Gateway
- VPC
- CloudWatch

Commands:

```bash
cd terraform
terraform init
terraform fmt -check -recursive
terraform validate
terraform plan -var="github_org=<your-org>" -var="github_repo=<your-repo>"
terraform apply -var="github_org=<your-org>" -var="github_repo=<your-repo>"
terraform destroy -var="github_org=<your-org>" -var="github_repo=<your-repo>"
```

`terraform apply` and `terraform destroy` are manual only.

## GitHub Actions

Included checks:

- `ruff check`
- `pytest`
- Docker build
- `docker compose config`
- `terraform fmt -check`
- `terraform validate`
- conditional `terraform plan`

The workflows do not run `terraform apply` or `terraform destroy`.

## Portfolio Summary

This project demonstrates a local-first agent platform that combines FastAPI, LangGraph, SQLite, Docker Compose, Terraform IAM practice, and GitHub Actions validation without introducing paid AWS runtime resources.
