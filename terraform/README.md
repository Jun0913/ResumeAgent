# Terraform IAM 범위

이 디렉터리는 Resume Agent Platform 포트폴리오 프로젝트의 AWS IAM 실습용 Terraform 코드만 포함합니다.

## 포함된 리소스

- GitHub Actions OIDC Provider
- GitHub Actions Assume Role
- GitHub Actions용 IAM Policy
- 실습용 IAM User
- 실습용 IAM Group
- IAM Policy Attachment

## 포함하지 않는 리소스

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

## 로컬 검증 상태

현재까지 확인한 항목:

- `terraform fmt -check -recursive`
- `terraform init -backend=false`
- `terraform validate`
- `terraform plan`
- `terraform apply`
- `terraform destroy`

`plan`, `apply`, `destroy`는 모두 수동으로 실행했습니다.

## 사용 방법

초기화와 검증:

```bash
terraform init -backend=false
terraform fmt -check -recursive
terraform validate
terraform plan -var="github_org=<your-org>" -var="github_repo=<your-repo>"
```

수동 적용:

```bash
terraform apply -var="github_org=<your-org>" -var="github_repo=<your-repo>"
```

수동 정리:

```bash
terraform destroy -var="github_org=<your-org>" -var="github_repo=<your-repo>"
```

## 주의 사항

- `terraform apply`와 `terraform destroy`는 GitHub Actions에서 자동 실행하지 않습니다.
- 이 프로젝트는 비용이 발생할 수 있는 AWS 런타임 리소스를 만들지 않습니다.
- 실제 GitHub Actions OIDC 연동은 별도 검증 단계로 남겨두었습니다.
