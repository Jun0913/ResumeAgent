variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "resume-agent-platform"
}

variable "aws_region" {
  description = "AWS region for IAM and OIDC resources"
  type        = string
  default     = "ap-northeast-2"
}

variable "github_org" {
  description = "GitHub organization or username"
  type        = string
}

variable "github_repo" {
  description = "GitHub repository name"
  type        = string
}
