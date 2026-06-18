output "github_actions_role_arn" {
  description = "IAM role ARN for GitHub Actions OIDC"
  value       = aws_iam_role.github_actions.arn
}

output "resume_agent_user_name" {
  description = "Practice IAM user name"
  value       = aws_iam_user.resume_agent.name
}

output "resume_agent_group_name" {
  description = "Practice IAM group name"
  value       = aws_iam_group.resume_agent.name
}
