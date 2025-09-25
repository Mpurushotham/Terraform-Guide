## Documentation Automation

Automate generation and validation of module documentation using `terraform-docs` and `pre-commit`.

### terraform-docs

Install:

```bash
curl -sSLo /usr/local/bin/terraform-docs https://github.com/terraform-docs/terraform-docs/releases/download/v0.18.0/terraform-docs-v0.18.0-linux-amd64
chmod +x /usr/local/bin/terraform-docs
```

Run in a module directory:

```bash
terraform-docs markdown table . > README.md
```

### pre-commit Configuration

`.pre-commit-config.yaml` example:

```yaml
repos:
  - repo: https://github.com/antonbabenko/pre-commit-terraform
    rev: v1.90.1
    hooks:
      - id: terraform_fmt
      - id: terraform_validate
      - id: terraform_tflint
      - id: terraform_tfsec
      - id: terraform_checkov
  - repo: https://github.com/terraform-docs/terraform-docs
    rev: v0.18.0
    hooks:
      - id: terraform-docs-go
        args: ["markdown", "table", "--output-file", "README.md", "--output-mode", "replace", "."]
```

Usage:

```bash
pipx install pre-commit
pre-commit install
pre-commit run --all-files | cat
```

