# Infra & Deployment

This folder contains Terraform config to:

- Create S3 bucket for:
  - Frontend static website
  - Sample data JSON files
- Create 4 Lambda functions (chat + 3 tools)
- Create API Gateway endpoint `/chat`
- Wire IAM permissions (Lambda → S3 → Bedrock)

## Usage (example)

```bash
cd infra-deploy/terraform
terraform init
terraform apply -var="project_prefix=utd-ai-campus"
