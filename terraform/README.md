# Terraform IAM Scope

This directory is intentionally limited to AWS IAM practice resources for the Resume Agent Platform portfolio project.

Included resources:

- GitHub Actions OIDC provider
- GitHub Actions assume role
- IAM policy for GitHub Actions role
- Practice IAM user
- Practice IAM group
- IAM policy attachment

Excluded resources:

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

## Usage

Initialize and validate:

```bash
terraform init
terraform fmt -check
terraform validate
terraform plan -var="github_org=<your-org>" -var="github_repo=<your-repo>"
```

Manual apply:

```bash
terraform apply -var="github_org=<your-org>" -var="github_repo=<your-repo>"
```

Manual destroy:

```bash
terraform destroy -var="github_org=<your-org>" -var="github_repo=<your-repo>"
```

`terraform apply` and `terraform destroy` must be run manually. They are not automated in GitHub Actions for this project.
