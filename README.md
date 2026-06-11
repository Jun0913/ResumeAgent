# Resume Agent Platform

## 1. Project Overview

Resume Agent Platform은 지원자의 경험과 채용공고를 입력받아, 여러 AI Agent가 역할을 나누어 자기소개서 초안을 생성하고 검토한 뒤 최종본을 만드는 로컬 기반 AI Agent 서비스입니다.

이 프로젝트의 핵심 목적은 단순히 자기소개서를 생성하는 것이 아니라, 다음 역량을 포트폴리오로 보여주는 것입니다.

* Python 기반 API 서버 개발
* LangGraph 기반 Multi-Agent Workflow 설계
* Docker Compose 기반 로컬 실행 환경 구성
* Terraform 기반 AWS IAM 리소스 코드화
* GitHub Actions 기반 CI 자동화
* 비용이 발생할 수 있는 AWS 리소스를 사용하지 않는 안전한 인프라 실습

---

## 2. Project Goal

이 프로젝트는 클라우드/인프라 엔지니어 포트폴리오용 프로젝트입니다.

따라서 기능 구현뿐만 아니라 다음 내용을 명확히 보여주어야 합니다.

1. AI Agent 서비스를 로컬에서 실행 가능한 구조로 구현한다.
2. 여러 Agent가 단계별로 역할을 나누어 자기소개서를 생성한다.
3. Docker Compose로 API 서버와 로컬 저장소를 실행한다.
4. Terraform으로 AWS IAM 리소스를 생성하고 삭제하는 실습을 제공한다.
5. GitHub Actions로 테스트, 코드 검사, Docker 빌드, Terraform 검증을 자동화한다.
6. AWS 비용 발생 가능성을 최소화한다.

---

## 3. Cost Control Policy

이 프로젝트는 비용 발생을 최소화해야 합니다.

### 반드시 지켜야 할 원칙

* 기본 실행 환경은 로컬이어야 합니다.
* Docker Compose 기반으로 실행해야 합니다.
* AWS에서 비용이 발생할 수 있는 리소스는 생성하지 않습니다.
* Terraform은 AWS IAM 리소스 중심으로만 작성합니다.
* GitHub Actions에서 `terraform apply`는 자동 실행하지 않습니다.
* `terraform apply`와 `terraform destroy`는 사용자가 수동으로 실행하도록 문서화합니다.
* LLM API 사용 비용을 피하기 위해 기본 모드는 `mock` 모드로 동작해야 합니다.
* 실제 LLM 호출은 사용자가 API Key를 제공한 경우에만 선택적으로 동작해야 합니다.

### 생성하면 안 되는 AWS 리소스

다음 리소스는 1차 구현 범위에서 생성하지 마세요.

* EC2
* ECS
* ECR
* S3
* RDS
* DynamoDB
* SQS
* Lambda
* ALB
* NAT Gateway
* VPC
* CloudWatch Log Group
* API Gateway
* Bedrock 실제 호출 환경

### 허용되는 AWS 리소스

Terraform 실습용으로 다음 IAM 리소스만 허용합니다.

* IAM User
* IAM Group
* IAM Policy
* IAM Role
* IAM Policy Attachment
* GitHub Actions OIDC Provider
* GitHub Actions용 Assume Role

---

## 4. Technology Stack

### Core Stack

| Area                | Technology        |
| ------------------- | ----------------- |
| Language            | Python            |
| API Framework       | FastAPI           |
| Agent Framework     | LangGraph         |
| Data Validation     | Pydantic          |
| Local Database      | SQLite            |
| Output Storage      | Local File System |
| Container           | Docker            |
| Local Orchestration | Docker Compose    |
| IaC                 | Terraform         |
| Cloud Scope         | AWS IAM only      |
| CI                  | GitHub Actions    |
| IDE                 | VS Code           |

---

## 5. Reason for Technology Choices

### Python

Python은 FastAPI, LangGraph, LangChain 계열 라이브러리와 잘 맞기 때문에 사용합니다. AI Agent 서비스와 API 서버를 같은 언어로 구현하여 구조를 단순하게 유지합니다.

### FastAPI

FastAPI는 Python 기반 API 서버를 빠르게 만들 수 있고, Pydantic 모델과 타입 힌트를 활용해 요청/응답 구조를 명확하게 정의할 수 있습니다. 또한 `/docs` 경로에서 Swagger UI를 통해 API를 바로 테스트할 수 있으므로, 별도의 프론트엔드 없이도 초기 시연이 가능합니다.

### LangGraph

LangGraph는 여러 단계를 가진 상태 기반 Agent Workflow를 구현하기 위해 사용합니다. 이 프로젝트는 단순한 LLM 호출이 아니라 다음 흐름을 가져야 합니다.

```text
채용공고 분석
→ 사용자 경험 분석
→ 요구사항과 경험 매칭
→ 자기소개서 초안 작성
→ 리뷰
→ 최종 수정
```

이런 단계형 Workflow는 Agent를 노드처럼 연결하고 상태를 전달하는 구조가 적합합니다.

### Docker Compose

이 프로젝트는 비용을 줄이기 위해 AWS 배포가 아니라 로컬 실행을 우선합니다. Docker Compose를 사용하면 FastAPI 서버와 로컬 볼륨, SQLite 저장소를 하나의 명령으로 실행할 수 있습니다.

### SQLite

비용이 발생하는 외부 DB를 사용하지 않기 위해 SQLite를 사용합니다. 작업 상태, 입력값, 생성 결과 메타데이터를 로컬 파일 기반 DB에 저장합니다.

### Terraform

Terraform은 AWS 인프라를 코드로 관리하는 실습을 위해 사용합니다. 다만 비용 방지를 위해 ECS, EC2, S3 같은 리소스는 만들지 않고 IAM 리소스만 코드화합니다.

### GitHub Actions

GitHub Actions는 다음 자동화를 위해 사용합니다.

* Python 테스트
* 코드 포맷 검사
* Docker 이미지 빌드 테스트
* Terraform fmt
* Terraform validate
* Terraform plan

단, 비용 방지를 위해 `terraform apply`는 자동 실행하지 않습니다.

---

## 6. System Architecture

### Local Architecture

```text
User
  ↓
FastAPI Swagger UI
  ↓
Resume Generation API
  ↓
LangGraph Multi-Agent Workflow
  ↓
SQLite
  ↓
Local outputs directory
```

### Optional Future Cloud Architecture

아래 구조는 추후 확장용 문서화만 합니다. 1차 구현에서는 만들지 않습니다.

```text
GitHub Actions
  ↓
AWS IAM OIDC Role
  ↓
Future AWS Deployment
```

---

## 7. Agent Workflow

LangGraph를 사용하여 다음 Agent들을 구현합니다.

### 7.1 JobAnalyzerAgent

채용공고를 분석합니다.

입력:

* 회사명
* 직무명
* 채용공고 본문

출력:

* 핵심 요구역량
* 우대사항
* 기술 키워드
* 인성/태도 키워드
* 자기소개서에 반영해야 할 포인트

---

### 7.2 ProfileAnalyzerAgent

사용자의 경험과 기술스택을 분석합니다.

입력:

* 사용자 경험
* 프로젝트 경험
* 기술스택
* 자격증
* 교육 이수 내용

출력:

* 강조 가능한 경험
* 직무 관련 기술
* 정량화 가능한 성과
* 부족한 부분
* 자기소개서에 사용할 수 있는 소재

---

### 7.3 MatchingAgent

채용공고 요구사항과 사용자 경험을 매칭합니다.

입력:

* JobAnalyzerAgent 결과
* ProfileAnalyzerAgent 결과

출력:

* 요구역량별 매칭 경험
* 강조할 경험 우선순위
* 자기소개서 핵심 메시지
* 피해야 할 과장 표현

---

### 7.4 DraftWriterAgent

자기소개서 초안을 작성합니다.

입력:

* 매칭 결과
* 글자 수 제한
* 문항
* 원하는 톤

출력:

* 자기소개서 1차 초안

---

### 7.5 ReviewAgent

초안을 검토합니다.

검토 기준:

* 채용공고와 관련성이 있는가
* 사용자의 경험이 구체적인가
* 문장이 과장되지 않았는가
* 클라우드/인프라 직무에 맞는가
* 문항에 대한 답변이 명확한가

출력:

* 개선점
* 위험한 표현
* 보완할 내용
* 점수

---

### 7.6 FinalEditorAgent

최종 자기소개서를 다듬습니다.

입력:

* 초안
* 리뷰 결과

출력:

* 최종 자기소개서
* 수정 요약
* 핵심 키워드

---

## 8. Workflow Rule

기본 Workflow는 다음과 같습니다.

```text
START
  ↓
JobAnalyzerAgent
  ↓
ProfileAnalyzerAgent
  ↓
MatchingAgent
  ↓
DraftWriterAgent
  ↓
ReviewAgent
  ↓
FinalEditorAgent
  ↓
END
```

추후 확장 가능한 조건 분기:

```text
Review score < threshold
  → DraftWriterAgent로 되돌아가 재작성

Review score >= threshold
  → FinalEditorAgent로 이동
```

1차 구현에서는 조건 분기를 단순화해도 됩니다. 단, 코드 구조는 추후 조건 분기를 추가할 수 있게 작성합니다.

---

## 9. LLM Provider Policy

비용 문제를 피하기 위해 기본 모드는 `mock`입니다.

### 기본 모드

```text
LLM_PROVIDER=mock
```

mock 모드에서는 실제 LLM API를 호출하지 않습니다. 대신 미리 정의한 템플릿 기반 응답을 반환합니다.

### 선택 모드

```text
LLM_PROVIDER=openai
```

사용자가 `OPENAI_API_KEY`를 제공한 경우에만 실제 LLM 호출을 허용합니다.

### 구현 요구사항

* `app/services/llm/base.py`에 공통 인터페이스를 둡니다.
* `app/services/llm/mock_client.py`를 기본 구현체로 둡니다.
* `app/services/llm/openai_client.py`는 선택 구현체로 둡니다.
* API Key가 없는데 `openai` 모드를 사용하면 명확한 에러 메시지를 반환합니다.
* API Key는 코드에 하드코딩하지 않습니다.

---

## 10. API Design

### Health Check

```http
GET /health
```

응답 예시:

```json
{
  "status": "ok"
}
```

---

### Create Resume Generation Job

```http
POST /api/v1/resume-jobs
```

요청 예시:

```json
{
  "company_name": "Example Company",
  "position": "Cloud Engineer",
  "job_description": "AWS, Linux, Docker, Terraform 경험 우대",
  "user_profile": {
    "summary": "AWS 기초 교육 이수, Docker 기반 프로젝트 경험",
    "skills": ["Python", "FastAPI", "Docker", "Terraform", "Linux"],
    "projects": [
      {
        "name": "AdCheck",
        "description": "허위광고 탐지 시스템 배포 경험",
        "role": "Backend and deployment"
      }
    ],
    "certifications": ["Linux Master Level 2", "정보처리기사 필기"]
  },
  "question": "지원동기와 직무 역량을 작성해주세요.",
  "max_length": 700,
  "tone": "담백하고 실무 중심"
}
```

응답 예시:

```json
{
  "job_id": "uuid",
  "status": "completed",
  "result": {
    "final_answer": "...",
    "review_summary": "...",
    "keywords": ["AWS", "Docker", "Terraform", "Linux"]
  }
}
```

---

### Get Job Result

```http
GET /api/v1/resume-jobs/{job_id}
```

응답 예시:

```json
{
  "job_id": "uuid",
  "status": "completed",
  "input": {},
  "result": {},
  "created_at": "2026-06-11T00:00:00"
}
```

---

## 11. Data Storage

SQLite를 사용합니다.

### Table: resume_jobs

| Column       | Type | Description                         |
| ------------ | ---- | ----------------------------------- |
| id           | TEXT | Job ID                              |
| status       | TEXT | pending, running, completed, failed |
| company_name | TEXT | 회사명                                 |
| position     | TEXT | 지원 직무                               |
| input_json   | TEXT | 전체 입력값                              |
| result_json  | TEXT | 결과값                                 |
| created_at   | TEXT | 생성일                                 |
| updated_at   | TEXT | 수정일                                 |

### Local Output

최종 결과물은 아래 경로에도 저장합니다.

```text
outputs/{job_id}.json
outputs/{job_id}.md
```

---

## 12. Directory Structure

다음 구조로 프로젝트를 생성합니다.

```text
resume-agent-platform/
  ├── README.md
  ├── .env.example
  ├── .gitignore
  ├── docker-compose.yml
  ├── Dockerfile
  ├── pyproject.toml
  ├── requirements.txt
  ├── app/
  │   ├── main.py
  │   ├── core/
  │   │   ├── config.py
  │   │   └── logging.py
  │   ├── api/
  │   │   ├── routes/
  │   │   │   ├── health.py
  │   │   │   └── resume_jobs.py
  │   │   └── schemas/
  │   │       └── resume.py
  │   ├── agents/
  │   │   ├── state.py
  │   │   ├── graph.py
  │   │   ├── job_analyzer.py
  │   │   ├── profile_analyzer.py
  │   │   ├── matching.py
  │   │   ├── draft_writer.py
  │   │   ├── reviewer.py
  │   │   └── final_editor.py
  │   ├── services/
  │   │   ├── llm/
  │   │   │   ├── base.py
  │   │   │   ├── mock_client.py
  │   │   │   └── openai_client.py
  │   │   ├── storage.py
  │   │   └── resume_service.py
  │   └── db/
  │       ├── database.py
  │       └── models.py
  ├── data/
  │   └── resume_agent.db
  ├── outputs/
  │   └── .gitkeep
  ├── tests/
  │   ├── test_health.py
  │   ├── test_resume_jobs.py
  │   └── test_agents.py
  ├── terraform/
  │   ├── README.md
  │   ├── versions.tf
  │   ├── providers.tf
  │   ├── variables.tf
  │   ├── main.tf
  │   ├── outputs.tf
  │   └── iam/
  │       ├── github_oidc.tf
  │       ├── github_actions_role.tf
  │       ├── policy.tf
  │       └── user_group.tf
  └── .github/
      └── workflows/
          ├── ci.yml
          └── terraform-check.yml
```

---

## 13. Environment Variables

`.env.example` 파일을 생성합니다.

```env
APP_NAME=resume-agent-platform
APP_ENV=local
LOG_LEVEL=INFO

LLM_PROVIDER=mock
OPENAI_API_KEY=

DATABASE_URL=sqlite:///./data/resume_agent.db
OUTPUT_DIR=./outputs
```

---

## 14. Local Development

### 14.1 Run without Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Windows PowerShell 예시:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

접속:

```text
http://localhost:8000/docs
```

---

### 14.2 Run with Docker Compose

```bash
docker compose up --build
```

접속:

```text
http://localhost:8000/docs
```

종료:

```bash
docker compose down
```

---

## 15. Docker Requirements

### Dockerfile

* Python slim 이미지 사용
* requirements 설치
* FastAPI 앱 실행
* 기본 포트 8000 사용

### docker-compose.yml

필수 서비스:

```text
api
```

필수 볼륨:

```text
./data:/app/data
./outputs:/app/outputs
```

주의:

* 외부 유료 DB를 사용하지 않습니다.
* Redis, PostgreSQL, MySQL 컨테이너는 1차 구현에서 사용하지 않습니다.
* 단일 API 컨테이너만으로 실행되게 만듭니다.

---

## 16. Terraform Scope

Terraform은 AWS IAM 실습만 담당합니다.

### Terraform으로 만들 리소스

* GitHub Actions OIDC Provider
* GitHub Actions용 IAM Role
* 최소 권한 IAM Policy
* 실습용 IAM Group
* 실습용 IAM User
* Policy Attachment

### Terraform으로 만들면 안 되는 리소스

* EC2
* ECS
* ECR
* S3
* DynamoDB
* RDS
* SQS
* Lambda
* VPC
* Subnet
* NAT Gateway
* ALB
* CloudWatch

### Terraform 명령어

```bash
cd terraform
terraform init
terraform fmt
terraform validate
terraform plan
```

실제 생성:

```bash
terraform apply
```

삭제:

```bash
terraform destroy
```

### Important

`terraform apply`를 실행했다면 반드시 실습 후 `terraform destroy`를 실행할 수 있도록 문서화합니다.

---

## 17. Terraform Variables

`terraform/variables.tf`에는 다음 변수를 둡니다.

```hcl
variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "resume-agent-platform"
}

variable "github_org" {
  description = "GitHub organization or username"
  type        = string
}

variable "github_repo" {
  description = "GitHub repository name"
  type        = string
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-2"
}
```

---

## 18. GitHub Actions

### CI Workflow

`.github/workflows/ci.yml`

필수 작업:

* Python 설치
* 의존성 설치
* 테스트 실행
* Docker build 테스트

실행 조건:

```text
push
pull_request
```

---

### Terraform Check Workflow

`.github/workflows/terraform-check.yml`

필수 작업:

* terraform fmt -check
* terraform init
* terraform validate
* terraform plan

주의:

* `terraform apply`는 자동 실행하지 않습니다.
* PR에서는 plan까지만 실행합니다.
* AWS credential이 없을 경우에도 fmt/validate는 동작하도록 구성합니다.
* OIDC 기반 AWS Role Assume은 추후 확장으로 남깁니다.

---

## 19. Testing Requirements

pytest 기반 테스트를 작성합니다.

필수 테스트:

```text
GET /health returns 200
POST /api/v1/resume-jobs returns completed job in mock mode
Agent graph returns final answer
SQLite job is saved
Output markdown/json file is created
```

테스트 실행:

```bash
pytest
```

---

## 20. Code Style

권장 도구:

* ruff
* pytest

명령어:

```bash
ruff check .
pytest
```

---

## 21. VS Code Setup

권장 확장:

* Python
* Pylance
* Docker
* HashiCorp Terraform
* YAML
* GitHub Actions
* Markdown All in One

`.vscode/extensions.json` 파일을 생성해 추천 확장을 명시해도 됩니다.

---

## 22. Implementation Order for Codex

다음 순서대로 구현하세요.

### Step 1. Project Skeleton

* 디렉터리 구조 생성
* FastAPI 기본 앱 생성
* `/health` API 구현
* `.env.example` 생성
* `.gitignore` 생성

### Step 2. Schema and Storage

* Pydantic 요청/응답 모델 구현
* SQLite 연결 구현
* `resume_jobs` 테이블 생성
* Local output 저장 기능 구현

### Step 3. LLM Client Abstraction

* Base LLM Client 인터페이스 생성
* Mock LLM Client 구현
* OpenAI Client는 선택 구현체로 작성
* 기본값은 반드시 mock

### Step 4. LangGraph Agent Workflow

* Agent State 정의
* JobAnalyzerAgent 구현
* ProfileAnalyzerAgent 구현
* MatchingAgent 구현
* DraftWriterAgent 구현
* ReviewAgent 구현
* FinalEditorAgent 구현
* Graph 연결

### Step 5. Resume Job API

* `POST /api/v1/resume-jobs` 구현
* `GET /api/v1/resume-jobs/{job_id}` 구현
* 생성 결과를 SQLite와 outputs 폴더에 저장

### Step 6. Docker

* Dockerfile 작성
* docker-compose.yml 작성
* `docker compose up --build`로 실행 가능하게 구성

### Step 7. Tests

* health check 테스트
* resume job 생성 테스트
* agent workflow 테스트
* storage 테스트

### Step 8. Terraform

* IAM 전용 Terraform 코드 작성
* GitHub OIDC Provider 코드 작성
* GitHub Actions Role 코드 작성
* 최소 권한 정책 코드 작성
* README에 apply/destroy 절차 작성

### Step 9. GitHub Actions

* Python CI 작성
* Docker build test 작성
* Terraform fmt/validate/plan workflow 작성
* apply 자동 실행 금지

### Step 10. Documentation

* README 실행 방법 정리
* 비용 방지 정책 정리
* 아키텍처 설명 정리
* 포트폴리오 설명 문장 추가

---

## 23. Acceptance Criteria

프로젝트는 다음 조건을 만족해야 합니다.

### Local App

* `uvicorn app.main:app --reload`로 실행된다.
* `docker compose up --build`로 실행된다.
* `GET /health`가 정상 응답한다.
* Swagger UI에서 자기소개서 생성 API를 테스트할 수 있다.
* mock 모드에서 실제 LLM API 비용 없이 결과가 생성된다.
* 결과가 SQLite에 저장된다.
* 결과가 `outputs/` 폴더에 json과 markdown으로 저장된다.

### Agent Workflow

* 최소 6개 Agent가 분리되어 있다.
* Agent별 입력과 출력 역할이 명확하다.
* LangGraph 기반 workflow로 연결되어 있다.
* 최종 결과에는 자기소개서, 리뷰 요약, 키워드가 포함된다.

### Terraform

* IAM 리소스만 포함한다.
* 비용 발생 가능성이 있는 AWS 리소스를 만들지 않는다.
* `terraform fmt`, `terraform validate`, `terraform plan`이 가능하다.
* `terraform destroy` 절차가 문서화되어 있다.

### GitHub Actions

* Python test workflow가 있다.
* Docker build test가 있다.
* Terraform check workflow가 있다.
* `terraform apply`는 자동 실행하지 않는다.

---

## 24. Portfolio Description

이 프로젝트를 이력서에 적을 때 사용할 수 있는 설명입니다.

```text
LangGraph 기반 Multi-Agent 자기소개서 생성 플랫폼을 구현했습니다. 채용공고 분석, 사용자 경험 분석, 요구역량 매칭, 초안 작성, 리뷰, 최종 편집 단계를 Agent Workflow로 분리하여 설계했습니다. 서비스는 FastAPI와 Docker Compose 기반으로 로컬 실행 가능하게 구성했으며, SQLite와 로컬 파일 시스템을 사용해 비용 발생 없이 결과를 저장했습니다. 또한 Terraform으로 AWS IAM 리소스를 코드화하고 GitHub Actions로 테스트, Docker 빌드, Terraform 검증을 자동화하여 클라우드/인프라 엔지니어에게 필요한 IaC와 CI 자동화 경험을 프로젝트에 반영했습니다.
```

---

## 25. Out of Scope

1차 구현에서 제외합니다.

* 프론트엔드 UI
* 실제 AWS 서비스 배포
* ECS/Fargate 배포
* ECR 이미지 푸시
* S3 저장
* DynamoDB 저장
* SQS 비동기 처리
* RDS 사용
* 사용자 로그인
* 결제 기능
* 운영 환경 배포
* Kubernetes 배포

---

## 26. Future Improvements

추후 확장 아이디어입니다.

* React 또는 Next.js 프론트엔드 추가
* OpenAI API 실제 호출 모드 추가
* AWS Bedrock Provider 추가
* ECS Fargate 배포
* ECR 이미지 저장
* S3 결과 저장
* DynamoDB 작업 상태 저장
* SQS 기반 비동기 처리
* CloudWatch 로그 수집
* GitHub Actions OIDC 기반 AWS 배포
* Terraform dev/prod 환경 분리

---

## 27. Final Instruction for Codex

이 프로젝트는 비용을 최소화하는 로컬 우선 프로젝트입니다.

구현 중 AWS 비용이 발생할 수 있는 리소스를 생성하지 마세요.
Terraform은 IAM 리소스만 작성하세요.
GitHub Actions에서 terraform apply를 자동 실행하지 마세요.
LLM Provider 기본값은 반드시 mock으로 유지하세요.
실제 LLM API 호출은 사용자가 API Key를 명시적으로 제공한 경우에만 가능하게 만드세요.
