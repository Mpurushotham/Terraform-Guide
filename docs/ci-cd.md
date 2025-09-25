## CI/CD with Security Gates

Establish pipelines that enforce formatting, validation, linting, security scans, policy checks, planning, and controlled applies.

### Required Stages
- Format and validate (`terraform fmt -check`, `terraform validate`)
- Lint (`tflint`)
- Static security (`tfsec`, `checkov`)
- Policy-as-code (Conftest/OPA)
- Plan (artifact)
- Apply (protected branch, approval, least privilege role)

### GitHub Actions Example

```yaml
name: terraform

on:
  pull_request:
    branches: [ main ]
  push:
    branches: [ main ]

jobs:
  plan:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.9.5
      - name: Setup tools
        run: |
          curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
          curl -sSfL https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install.sh | sh -s -- -b /usr/local/bin latest
          pipx install checkov
          curl -L -o conftest.tar.gz https://github.com/open-policy-agent/conftest/releases/download/v0.59.0/conftest_Linux_x86_64.tar.gz && tar -xzf conftest.tar.gz -C /usr/local/bin conftest
      - name: Terraform init
        run: terraform init -input=false
      - name: Format & Validate
        run: |
          terraform fmt -check
          terraform validate
      - name: Lint
        run: tflint --no-color
      - name: Security Scans
        run: |
          tfsec . --no-color --soft-fail=false
          checkov -d . --quiet --compact
      - name: Policy Check
        run: conftest test . --policy policies
      - name: Plan
        run: terraform plan -out tfplan
      - name: Upload plan
        uses: actions/upload-artifact@v4
        with:
          name: tfplan
          path: tfplan

  apply:
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    runs-on: ubuntu-latest
    needs: [ plan ]
    environment:
      name: production
      url: https://example.internal
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.9.5
      - name: Download plan
        uses: actions/download-artifact@v4
        with:
          name: tfplan
          path: .
      - name: Apply
        run: terraform apply -input=false tfplan
```

### GitLab CI Example

```yaml
stages:
  - validate
  - plan
  - apply

variables:
  TF_IN_AUTOMATION: "true"

validate:
  stage: validate
  image: hashicorp/terraform:1.9.5
  script:
    - terraform init -input=false
    - terraform fmt -check
    - terraform validate
  rules:
    - if: $CI_PIPELINE_SOURCE == 'merge_request_event'

plan:
  stage: plan
  image: hashicorp/terraform:1.9.5
  script:
    - terraform init -input=false
    - terraform plan -out tfplan
  artifacts:
    paths:
      - tfplan
  rules:
    - if: $CI_PIPELINE_SOURCE == 'merge_request_event'

apply:
  stage: apply
  image: hashicorp/terraform:1.9.5
  script:
    - terraform init -input=false
    - terraform apply -input=false tfplan
  dependencies:
    - plan
  when: manual
  rules:
    - if: $CI_COMMIT_BRANCH == 'main'
```

### Secrets and Credentials
- Use OIDC-federated roles where supported (GitHub/GitLab -> Cloud provider). Avoid long-lived keys.
- Store sensitive values in secret managers; never commit credentials.

