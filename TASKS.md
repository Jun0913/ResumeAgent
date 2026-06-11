# TASKS.md

# Resume Agent Platform 작업 계획

## Step 1. FastAPI 기본 골격 만들기

* [ ] 프로젝트 기본 디렉터리 구조 생성
* [ ] FastAPI 앱 생성
* [ ] `GET /health` API 구현
* [ ] `.env.example` 생성
* [ ] `.gitignore` 생성
* [ ] `requirements.txt` 생성
* [ ] `app/core/config.py` 설정 파일 생성
* [ ] API 라우터 구조 생성
* [ ] pytest 기반 health check 테스트 작성

---

## Step 2. 자기소개서 생성 API 기본 구조 만들기

* [ ] Pydantic 요청/응답 스키마 생성
* [ ] `POST /api/v1/resume-jobs` API 구현
* [ ] `GET /api/v1/resume-jobs/{job_id}` API 구현
* [ ] 실제 LLM API 호출 없이 mock 응답 반환
* [ ] API 테스트 작성

---

## Step 3. SQLite 저장 구조 만들기

* [ ] SQLite 데이터베이스 연결 코드 작성
* [ ] `resume_jobs` 테이블 생성
* [ ] 자기소개서 생성 요청 입력값 저장
* [ ] 자기소개서 생성 결과 저장
* [ ] 생성 결과를 `outputs/` 폴더에 저장
* [ ] JSON 파일 저장 기능 구현
* [ ] Markdown 파일 저장 기능 구현
* [ ] 저장 기능 테스트 작성

---

## Step 4. LLM Client 추상화 구조 만들기

* [ ] 공통 LLM Client 인터페이스 생성
* [ ] Mock LLM Client 구현
* [ ] 선택 기능으로 OpenAI Client 구조 작성
* [ ] 기본값을 `LLM_PROVIDER=mock`으로 유지
* [ ] API Key가 없으면 실제 LLM API를 호출하지 않도록 처리
* [ ] API Key를 코드에 하드코딩하지 않도록 구성

---

## Step 5. LangGraph Agent Workflow 구현

* [ ] Agent State 정의
* [ ] JobAnalyzerAgent 구현
* [ ] ProfileAnalyzerAgent 구현
* [ ] MatchingAgent 구현
* [ ] DraftWriterAgent 구현
* [ ] ReviewAgent 구현
* [ ] FinalEditorAgent 구현
* [ ] LangGraph로 Agent 흐름 연결
* [ ] Agent Workflow 테스트 작성

---

## Step 6. Docker 로컬 실행 환경 구성

* [ ] Dockerfile 작성
* [ ] docker-compose.yml 작성
* [ ] `data/` 폴더 볼륨 연결
* [ ] `outputs/` 폴더 볼륨 연결
* [ ] `docker compose up --build` 실행 확인
* [ ] Docker 실행 방법을 README에 정리

---

## Step 7. Terraform IAM 실습 구성

* [ ] `terraform/` 디렉터리 생성
* [ ] AWS Provider 설정
* [ ] IAM User 예제 작성
* [ ] IAM Group 예제 작성
* [ ] IAM Policy 예제 작성
* [ ] GitHub Actions OIDC Provider 작성
* [ ] GitHub Actions Assume Role 작성
* [ ] Terraform 코드가 IAM 리소스만 생성하는지 확인
* [ ] `terraform apply` 실행 방법 문서화
* [ ] `terraform destroy` 삭제 방법 문서화

---

## Step 8. GitHub Actions CI 구성

* [ ] Python 테스트 Workflow 작성
* [ ] ruff 검사 추가
* [ ] pytest 실행 추가
* [ ] Docker build 검사 추가
* [ ] Terraform fmt 검사 추가
* [ ] Terraform validate 검사 추가
* [ ] Terraform plan 검사 추가
* [ ] `terraform apply` 자동 실행 금지 확인

---

## Step 9. 문서 정리

* [ ] README 실행 방법 업데이트
* [ ] 아키텍처 설명 업데이트
* [ ] 비용 방지 정책 업데이트
* [ ] Terraform 사용 범위 정리
* [ ] GitHub Actions 사용 범위 정리
* [ ] 이력서/포트폴리오용 프로젝트 설명 문장 추가
* [ ] 트러블슈팅 섹션 추가

---

## 전체 완료 기준

이 프로젝트는 다음 조건을 만족하면 1차 완료로 본다.

* [ ] 로컬에서 FastAPI 서버가 실행된다.
* [ ] `GET /health`가 정상 응답한다.
* [ ] mock 모드에서 자기소개서 생성 API가 동작한다.
* [ ] 실제 LLM API를 호출하지 않아도 테스트가 가능하다.
* [ ] 생성 결과가 SQLite에 저장된다.
* [ ] 생성 결과가 `outputs/` 폴더에 저장된다.
* [ ] LangGraph 기반 Agent Workflow가 동작한다.
* [ ] Docker Compose로 로컬 실행이 가능하다.
* [ ] Terraform은 AWS IAM 리소스만 관리한다.
* [ ] 비용이 발생할 수 있는 AWS 리소스를 생성하지 않는다.
* [ ] GitHub Actions에서 테스트와 검증이 자동 실행된다.
* [ ] GitHub Actions에서 `terraform apply`는 자동 실행되지 않는다.
