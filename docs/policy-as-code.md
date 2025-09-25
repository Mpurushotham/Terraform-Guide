## Policy as Code with OPA/Conftest

Codify guardrails to block insecure Terraform configurations before deployment.

### Directory Structure

```
policies/
  terraform/
    aws/
      s3_no_public.rego
    common/
      tags_required.rego
```

### Running Policies

```bash
conftest test . --policy policies
```

### Example Policies

S3 buckets must not be publicly readable:

```rego
package terraform.aws.s3_no_public

deny[msg] {
  input.resource_type == "aws_s3_bucket_public_access_block"
  block_public_acls := input.values.block_public_acls
  block_public_policy := input.values.block_public_policy
  ignore_public_acls := input.values.ignore_public_acls
  restrict_public_buckets := input.values.restrict_public_buckets
  not block_public_acls
  msg := sprintf("S3 public access not fully blocked for %s", [input.address])
}
```

Required tags on all taggable resources:

```rego
package terraform.common.tags_required

required = {"owner", "environment", "cost_center", "data_classification"}

deny[msg] {
  input.tags
  missing := required - {k | k := input.tags[_]}
  count(missing) > 0
  msg := sprintf("Resource %s missing required tags: %v", [input.address, missing])
}
```

### Authoring Guidance
- Scope policies to providers/services; keep messages actionable.
- Start in warn-only mode, then enforce.
- Version and test policies alongside modules.

