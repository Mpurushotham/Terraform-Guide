## Azure Examples Catalog

This catalog provides Terraform examples with Azure DevOps pipelines and Python verification scripts. Each example includes step-by-step instructions.

### Included Examples
- Resource Group: `examples/azure/resource-group`
- Storage Account: `examples/azure/storage-account`
- AKS (Kubernetes): `examples/azure/aks`

More services can be added following the same pattern.

### Common Pipeline Variables
- `AZURE_SERVICE_CONNECTION`: Azure DevOps ARM service connection name
- Resource-specific names (e.g., `RESOURCE_GROUP_NAME`, `STORAGE_ACCOUNT_NAME`)

### Common Commands
```bash
terraform init
terraform plan -out tfplan
terraform apply tfplan
```

