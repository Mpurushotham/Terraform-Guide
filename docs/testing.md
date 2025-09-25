## Testing Strategy for Terraform

Combine native validation, linting, and unit/integration testing to ensure correctness and security.

### Levels
- Format & Validate: `terraform fmt -check`, `terraform validate`
- Lint: `tflint`
- Security: `tfsec`, `checkov`
- Unit tests: `terraform plan` snapshot comparisons
- Integration tests: Terratest (Golang) applying to ephemeral environments

### Terratest Skeleton

```go
package test

import (
  "testing"
  "github.com/gruntwork-io/terratest/modules/terraform"
  "github.com/stretchr/testify/require"
)

func TestModuleBasic(t *testing.T) {
  t.Parallel()
  options := &terraform.Options{
    TerraformDir: "../../modules/<module>/examples/basic",
    Vars: map[string]interface{}{
      "environment": "test",
    },
  }
  defer terraform.Destroy(t, options)
  terraform.InitAndApply(t, options)

  vpcId := terraform.Output(t, options, "vpc_id")
  require.NotEmpty(t, vpcId)
}
```

### Best Practices
- Run destructive tests only in dedicated test accounts.
- Use small CIDRs and cost controls for ephemeral infra.
- Parallelize where possible; isolate state per test.

