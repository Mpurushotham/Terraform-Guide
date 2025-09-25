## Governance, Tagging, and Cost Controls

### Tagging Baseline
- Required tags: `owner`, `environment`, `cost_center`, `data_classification`
- Enforce via module inputs and OPA policies.

Example:

```hcl
locals {
  required_tags = {
    owner               = var.owner
    environment         = var.environment
    cost_center         = var.cost_center
    data_classification = var.data_classification
  }
}

resource "aws_s3_bucket" "this" {
  bucket = var.name
  tags   = merge(local.required_tags, var.extra_tags)
}
```

### Cost Controls
- Use Infracost to estimate changes per PR.
- Prefer on-demand with rightsizing; restrict public egress.
- Use lifecycle policies, schedules, and serverless where viable.

#### Infracost in CI

```yaml
name: infracost
on: pull_request
jobs:
  infracost:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: infracost/actions/setup@v3
      - run: infracost breakdown --path . --format json --out-file infracost.json
      - uses: infracost/actions/comment@v3
        with:
          path: infracost.json
```

### Access Governance
- Separate plan/apply roles; limit human access to production.
- Record changes via PRs and plan artifacts.

