resource "aws_iam_group" "resume_agent" {
  name = "${var.project_name}-group"
}

resource "aws_iam_user" "resume_agent" {
  name = "${var.project_name}-user"
}

resource "aws_iam_user_group_membership" "resume_agent" {
  user   = aws_iam_user.resume_agent.name
  groups = [aws_iam_group.resume_agent.name]
}

data "aws_iam_policy_document" "resume_agent_user_permissions" {
  statement {
    sid    = "AllowOwnPasswordChange"
    effect = "Allow"
    actions = [
      "iam:ChangePassword",
      "iam:GetAccountPasswordPolicy",
      "iam:GetUser",
    ]
    resources = [
      "arn:aws:iam::*:user/${aws_iam_user.resume_agent.name}",
    ]
  }
}

resource "aws_iam_policy" "resume_agent_user_permissions" {
  name        = "${var.project_name}-user-policy"
  description = "Practice policy attached to the Resume Agent IAM group"
  policy      = data.aws_iam_policy_document.resume_agent_user_permissions.json
}

resource "aws_iam_group_policy_attachment" "resume_agent_user_permissions" {
  group      = aws_iam_group.resume_agent.name
  policy_arn = aws_iam_policy.resume_agent_user_permissions.arn
}
