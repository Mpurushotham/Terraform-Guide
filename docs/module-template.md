## Module README Template (terraform-docs compatible)

Copy this template to each module's `README.md` and use `terraform-docs` to auto-generate Inputs/Outputs/Resources.

```
# <module-name>

<one-line description>

## Usage

```hcl
module "example" {
  source = "<registry-namespace>/<module-name>/<provider>"

  # inputs ...
}
```

## Examples
- See `examples/basic` for a minimal configuration.

## Requirements
<!-- BEGIN_TF_DOCS -->
<!-- terraform-docs will inject the generated documentation below -->
<!-- END_TF_DOCS -->

## Security
- No public exposure by default; opt-in flags must be explicit (e.g., `enable_public_access = false` by default)
- Encryption at rest and in transit enabled where applicable
- Sensitive outputs are avoided; inputs marked `sensitive = true` when appropriate

## Inputs to highlight
- Ownership and tagging (`owner`, `environment`, `cost_center`, `data_classification`)
- Region and provider aliasing for multi-account setups

## Contributing
1. `terraform fmt -check`
2. `terraform validate`
3. `tflint`
4. `tfsec` and/or `checkov`
5. Update examples and run `terraform-docs` to refresh this README

```

### Recommended Module Layout

```
<module>/
  main.tf
  variables.tf
  outputs.tf
  versions.tf
  README.md
  examples/
    basic/
      main.tf
```

### Minimal `versions.tf`

```hcl
terraform {
  required_version = ">= 1.6, < 2.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

