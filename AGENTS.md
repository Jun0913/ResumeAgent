# AGENTS.md

## 프로젝트 개요

이 저장소는 `Resume Agent Platform` 프로젝트입니다.

이 프로젝트는 클라우드/인프라 엔지니어 포트폴리오용으로 만드는 로컬 우선 AI Agent 서비스입니다.

이 프로젝트에서 보여줘야 할 핵심 역량은 다음과 같습니다.

* FastAPI 기반 API 개발
* LangGraph 기반 Multi-Agent Workflow 설계
* Docker Compose 기반 로컬 실행 환경 구성
* Terraform 기반 AWS IAM 실습
* GitHub Actions 기반 CI 자동화
* 비용 발생을 최소화하는 인프라 설계

---

## 핵심 규칙

* 이 프로젝트는 로컬 실행을 우선합니다.
* 사용 기술은 Python, FastAPI, LangGraph, Pydantic, SQLite, Docker Compose, Terraform, GitHub Actions를 기준으로 합니다.
* 기본 LLM Provider는 반드시 `mock`으로 유지합니다.
* 사용자가 API Key를 명시적으로 제공하고 설정을 변경한 경우에만 실제 LLM API 호출을 허용합니다.
* API Key나 secret 값은 코드에 하드코딩하지 않습니다.
* 1차 구현에서는 프론트엔드를 추가하지 않습니다.
* 1차 구현에서는 PostgreSQL, MySQL, Redis, Celery, Kubernetes, ECS, 외부 managed service를 추가하지 않습니다.

---

## AWS 비용 방지 규칙

* Terraform은 AWS IAM 리소스만 관리해야 합니다.
* 비용이 발생할 수 있는 AWS 리소스를 생성하지 않습니다.
* 다음 AWS 리소스는 생성하지 않습니다.

```text
EC2
ECS
ECR
S3
RDS
DynamoDB
SQS
Lambda
ALB
NAT Gateway
VPC
CloudWatch
```

* 비용이 발생할 가능성이 있는 Terraform 코드를 추가하지 않습니다.
* `terraform apply`를 자동 실행하지 않습니다.
* 문서에서 `terraform apply`를 안내할 경우, 반드시 `terraform destroy`도 함께 안내합니다.

---

## 필수 API

다음 API는 반드시 구현 대상입니다.

```text
GET /health
POST /api/v1/resume-jobs
GET /api/v1/resume-jobs/{job_id}
```

---

## 필수 Agent Workflow

LangGraph 기반 Agent Workflow는 다음 순서를 기준으로 합니다.

```text
JobAnalyzerAgent
→ ProfileAnalyzerAgent
→ MatchingAgent
→ DraftWriterAgent
→ ReviewAgent
→ FinalEditorAgent
```

Workflow의 최종 결과에는 다음 값이 포함되어야 합니다.

* 최종 자기소개서
* 리뷰 요약
* 추출 키워드
* job id
* status

---

## 프로젝트 구조 규칙

* API route 코드는 `app/api/routes/` 아래에 둡니다.
* Pydantic schema 코드는 `app/api/schemas/` 아래에 둡니다.
* Agent 코드는 `app/agents/` 아래에 둡니다.
* LLM client 코드는 `app/services/llm/` 아래에 둡니다.
* SQLite와 DB 관련 코드는 `app/db/` 아래에 둡니다.
* Terraform 코드는 `terraform/` 아래에 둡니다.
* GitHub Actions workflow는 `.github/workflows/` 아래에 둡니다.

---

## 저장 규칙

* 작업 메타데이터는 SQLite에 저장합니다.
* 생성 결과는 `outputs/` 폴더에 저장합니다.
* 생성 결과는 JSON과 Markdown 파일로 모두 저장합니다.
* 외부 managed database는 사용하지 않습니다.

---

## Terraform 규칙

Terraform 코드는 AWS IAM 실습만 담당합니다.

허용되는 AWS 리소스:

```text
IAM User
IAM Group
IAM Policy
IAM Role
IAM Policy Attachment
GitHub Actions OIDC Provider
GitHub Actions Assume Role
```

금지되는 AWS 리소스:

```text
EC2
ECS
ECR
S3
RDS
DynamoDB
SQS
Lambda
ALB
NAT Gateway
VPC
CloudWatch
```

---

## GitHub Actions 규칙

GitHub Actions에서 허용되는 작업:

```text
Python test
ruff check
Docker build check
Terraform fmt
Terraform validate
Terraform plan
```

GitHub Actions에서 자동 실행하면 안 되는 작업:

```text
terraform apply
terraform destroy
```

---

## 검증 규칙

코드를 변경한 뒤 가능한 경우 관련 검증 명령을 실행합니다.

일반 코드 변경 시:

```bash
ruff check .
pytest
docker compose config
```

Terraform 변경 시:

```bash
cd terraform
terraform fmt -check
terraform validate
```

명령을 실행할 수 없다면, 실행하지 못한 이유를 설명합니다.

---

## 완료 기준

작업은 다음 조건을 만족해야 완료로 봅니다.

* 로컬에서 앱이 실행됩니다.
* `/health`가 정상 응답합니다.
* 자기소개서 생성 기능은 mock 모드에서 동작합니다.
* 비용이 발생할 수 있는 AWS 리소스가 추가되지 않았습니다.
* Terraform은 IAM 리소스만 관리합니다.
* 기능 변경이 있다면 테스트가 추가되거나 수정되었습니다.
* 명령어, 구조, 실행 방법이 바뀌었다면 관련 문서가 업데이트되었습니다.
