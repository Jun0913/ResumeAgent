data "aws_iam_policy_document" "github_actions_permissions" {
  statement {
    sid    = "ReadOnlyIamListing"
    effect = "Allow"
    actions = [
      "iam:GetGroup",
      "iam:GetOpenIDConnectProvider",
      "iam:GetPolicy",
      "iam:GetPolicyVersion",
      "iam:GetRole",
      "iam:GetUser",
      "iam:ListAttachedRolePolicies",
      "iam:ListGroups",
      "iam:ListOpenIDConnectProviders",
      "iam:ListPolicies",
      "iam:ListRolePolicies",
      "iam:ListRoles",
      "iam:ListUsers",
    ]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "github_actions_permissions" {
  name        = "${var.project_name}-github-actions-policy"
  description = "Minimum IAM read-only permissions for Terraform validation and inspection"
  policy      = data.aws_iam_policy_document.github_actions_permissions.json
}

resource "aws_iam_role_policy_attachment" "github_actions_permissions" {
  role       = aws_iam_role.github_actions.name
  policy_arn = aws_iam_policy.github_actions_permissions.arn
}
