# Resume Agent Platform

Resume Agent Platform은 클라우드/인프라 엔지니어 포트폴리오를 위한 로컬 우선 AI 에이전트 프로젝트입니다. FastAPI API를 제공하고, LangGraph 기반 멀티 에이전트 워크플로를 기본 `mock` 모드로 실행하며, 작업 메타데이터는 SQLite에 저장하고 결과물은 로컬 JSON 및 Markdown 파일로 남깁니다.

## 개요

- FastAPI 기반 API 서버
- 6개 에이전트로 구성된 LangGraph 워크플로
- SQLite 기반 작업 저장
- 로컬 `outputs/` 결과 저장
- Docker Compose 기반 로컬 실행
- AWS IAM 범위로 제한된 Terraform 실습
- 검증 전용 GitHub Actions CI

## 현재 API

- `GET /health`
- `POST /api/v1/resume-jobs`
- `GET /api/v1/resume-jobs/{job_id}`

## 에이전트 워크플로

```text
JobAnalyzerAgent
-> ProfileAnalyzerAgent
-> MatchingAgent
-> DraftWriterAgent
-> ReviewAgent
-> FinalEditorAgent
```

최종 응답에는 다음 값이 포함됩니다.

- `job_id`
- `status`
- `keywords`
- `review_summary`
- `final_cover_letter`

## 프로젝트 구조

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

## 환경 변수

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

## 로컬 개발

### 가상환경으로 실행

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload
```

실행 후 접속:

```text
http://localhost:8000/docs
```

### 로컬 검증

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

마운트 볼륨:

- `./data:/app/data`
- `./outputs:/app/outputs`

## LLM Provider 정책

- 기본 provider는 `mock`
- `mock` 모드에서는 실제 LLM API를 호출하지 않음
- 실제 LLM 연동은 사용자가 API key를 명시적으로 제공하고 provider를 변경한 경우에만 허용
- 현재 `openai` 클라이언트는 가드가 있는 placeholder이며 실제 API를 호출하지 않음

## 저장 구조

- SQLite 데이터베이스: `data/resume_agent.db`
- JSON 결과 파일: `outputs/{job_id}.json`
- Markdown 결과 파일: `outputs/{job_id}.md`

## Terraform 범위

허용 리소스:

- IAM User
- IAM Group
- IAM Policy
- IAM Role
- IAM Policy Attachment
- GitHub Actions OIDC Provider
- GitHub Actions Assume Role

금지 리소스:

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

주요 명령:

```bash
cd terraform
terraform init
terraform fmt -check -recursive
terraform validate
terraform plan -var="github_org=<your-org>" -var="github_repo=<your-repo>"
terraform apply -var="github_org=<your-org>" -var="github_repo=<your-repo>"
terraform destroy -var="github_org=<your-org>" -var="github_repo=<your-repo>"
```

`terraform apply`와 `terraform destroy`는 수동 실행만 허용합니다.

## GitHub Actions

포함된 검증:

- `ruff check`
- `pytest`
- Docker build
- `docker compose config`
- `terraform fmt -check`
- `terraform validate`
- 조건부 `terraform plan`

GitHub Actions에서는 `terraform apply`와 `terraform destroy`를 자동 실행하지 않습니다.

## 현재 완료 상태

완료된 항목:

- FastAPI API 구현
- LangGraph 워크플로 구현
- SQLite 및 outputs 저장 구현
- Docker Compose 실행 검증
- Terraform `fmt`, `init`, `validate`, `plan`, `apply`, `destroy` 수동 검증
- GitHub Actions CI 실제 실행 확인

아직 남아 있는 항목:

- GitHub Actions와 AWS의 실제 OIDC 연동 확인
- GitHub repository secrets 또는 OIDC 기반 AWS 인증 최종 정리

## 포트폴리오 요약

이 프로젝트는 FastAPI, LangGraph, SQLite, Docker Compose, Terraform IAM 실습, GitHub Actions 검증을 결합한 로컬 우선 AI 에이전트 플랫폼입니다. 비용이 발생할 수 있는 AWS 런타임 리소스를 만들지 않고도 백엔드, 워크플로, 저장소, IaC, CI 구성을 함께 보여주는 포트폴리오 프로젝트를 목표로 합니다.
