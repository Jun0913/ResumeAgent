locals {
  github_repository = "${var.github_org}/${var.github_repo}"
}

module "iam" {
  source = "./iam"

  project_name      = var.project_name
  aws_region        = var.aws_region
  github_org        = var.github_org
  github_repo       = var.github_repo
  github_repository = local.github_repository
}
