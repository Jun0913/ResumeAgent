output "github_actions_role_arn" {
  description = "IAM role ARN for GitHub Actions OIDC"
  value       = module.iam.github_actions_role_arn
}

output "resume_agent_user_name" {
  description = "Practice IAM user name"
  value       = module.iam.resume_agent_user_name
}

output "resume_agent_group_name" {
  description = "Practice IAM group name"
  value       = module.iam.resume_agent_group_name
}
