# TASKS.md

# Resume Agent Platform 작업 현황

표기 기준:
- `[O]` 완료
- `[-]` 미완료

## Step 1. FastAPI 기본 골격

- [O] 프로젝트 기본 디렉터리 구조 생성
- [O] FastAPI 앱 생성
- [O] `GET /health` API 구현
- [O] `.env.example` 생성
- [O] `.gitignore` 생성
- [O] `requirements.txt` 생성
- [O] `app/core/config.py` 설정 파일 생성
- [O] API 라우트 구조 생성
- [O] pytest 기반 health check 테스트 작성

---

## Step 2. 자기소개서 생성 API 기본 구조

- [O] Pydantic 요청/응답 스키마 생성
- [O] `POST /api/v1/resume-jobs` API 구현
- [O] `GET /api/v1/resume-jobs/{job_id}` API 구현
- [O] 실제 LLM API 호출 없이 mock 응답 반환
- [O] API 테스트 작성

---

## Step 3. SQLite 저장 구조

- [O] SQLite 데이터베이스 연결 코드 작성
- [O] `resume_jobs` 테이블 생성
- [O] 자기소개서 생성 요청 입력값 저장
- [O] 자기소개서 생성 결과 저장
- [O] 생성 결과를 `outputs/` 폴더에 저장
- [O] JSON 파일 저장 기능 구현
- [O] Markdown 파일 저장 기능 구현
- [O] 저장 기능 테스트 작성

---

## Step 4. LLM Client 추상화 구조

- [O] 공통 LLM Client 인터페이스 생성
- [O] Mock LLM Client 구현
- [O] OpenAI Client 구조 작성
- [O] 기본값을 `LLM_PROVIDER=mock`으로 유지
- [O] API Key가 없으면 실제 LLM API를 호출하지 않도록 처리
- [O] API Key를 코드에 하드코딩하지 않도록 구성

---

## Step 5. LangGraph Agent Workflow

- [O] Agent State 정의
- [O] JobAnalyzerAgent 구현
- [O] ProfileAnalyzerAgent 구현
- [O] MatchingAgent 구현
- [O] DraftWriterAgent 구현
- [O] ReviewAgent 구현
- [O] FinalEditorAgent 구현
- [O] LangGraph로 Agent 흐름 연결
- [O] Agent Workflow 테스트 작성

---

## Step 6. Docker 로컬 실행 환경

- [O] Dockerfile 작성
- [O] `docker-compose.yml` 작성
- [O] `data/` 폴더 볼륨 연결
- [O] `outputs/` 폴더 볼륨 연결
- [O] `docker compose up --build` 실행 확인
- [O] Docker 실행 방법을 README에 정리

---

## Step 7. Terraform IAM 실습 구성

- [O] `terraform/` 디렉터리 생성
- [O] AWS Provider 설정
- [O] IAM User 예제 작성
- [O] IAM Group 예제 작성
- [O] IAM Policy 예제 작성
- [O] GitHub Actions OIDC Provider 작성
- [O] GitHub Actions Assume Role 작성
- [O] Terraform 코드가 IAM 리소스만 생성하는지 확인
- [O] `terraform apply` 실행 방법 문서화
- [O] `terraform destroy` 실행 방법 문서화
- [O] `terraform fmt -check -recursive` 검증
- [O] `terraform init -backend=false` 검증
- [O] `terraform validate` 검증
- [-] AWS 자격 증명으로 `terraform plan` 실제 실행 확인
- [-] AWS에 `terraform apply` 수동 실행

---

## Step 8. GitHub Actions CI 구성

- [O] Python 테스트 workflow 작성
- [O] `ruff` 검사 추가
- [O] `pytest` 실행 추가
- [O] Docker build 검사 추가
- [O] Terraform fmt 검사 추가
- [O] Terraform validate 검사 추가
- [O] Terraform plan 단계 추가
- [O] `terraform apply` 자동 실행 금지 확인
- [-] GitHub Actions 실제 실행 결과 확인
- [-] GitHub repository secrets 또는 OIDC 실제 연동

---

## Step 9. 문서 정리

- [O] README 실행 방법 업데이트
- [O] 아키텍처 설명 업데이트
- [O] 비용 방지 정책 업데이트
- [O] Terraform 사용 범위 정리
- [O] GitHub Actions 사용 범위 정리
- [O] 포트폴리오용 프로젝트 설명 문장 추가
- [O] 운영 범위 제외 섹션 반영

---

## 연동 상태 정리

### 이미 연동/구현된 것

- [O] FastAPI API
- [O] SQLite 저장
- [O] `outputs/` 파일 저장
- [O] LangGraph workflow
- [O] Docker Compose 로컬 실행 검증
- [O] Terraform IAM 코드 작성
- [O] Terraform 로컬 검증 (`fmt`, `init`, `validate`)
- [O] GitHub Actions workflow 파일 작성

### 아직 실제 연동하지 않은 것

- [-] AWS 계정에 실제 `terraform apply`
- [-] AWS 자격 증명으로 `terraform plan` 실행 확인
- [-] GitHub repository에 secrets 설정
- [-] GitHub Actions 실제 실행 확인
- [-] GitHub Actions와 AWS의 실제 OIDC 신뢰 연결 확인

---

## 전체 완료 기준

- [O] 로컬에서 FastAPI 서버가 실행된다
- [O] `GET /health`가 정상 응답한다
- [O] mock 모드에서 자기소개서 생성 API가 동작한다
- [O] 실제 LLM API를 호출하지 않아도 테스트가 가능하다
- [O] 생성 결과가 SQLite에 저장된다
- [O] 생성 결과가 `outputs/` 폴더에 저장된다
- [O] LangGraph 기반 Agent Workflow가 동작한다
- [O] Docker Compose로 로컬 실행이 가능하다
- [O] Terraform은 AWS IAM 리소스만 관리한다
- [O] 비용이 발생할 수 있는 AWS 리소스를 생성하지 않는다
- [O] GitHub Actions에서 테스트와 검증이 자동 실행되도록 파일이 구성되어 있다
- [O] GitHub Actions에서 `terraform apply`를 자동 실행하지 않는다
- [-] GitHub Actions 실제 실행 확인
- [-] AWS 실제 연동 확인
