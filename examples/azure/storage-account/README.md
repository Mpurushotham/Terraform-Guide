## Azure Storage Account (Terraform + Azure DevOps + Python Verify)

### What this example does
Creates a Resource Group and a secure Storage Account with TLS 1.2, soft delete for blobs, and no public access.

### Prerequisites
- Azure DevOps Service Connection `$(AZURE_SERVICE_CONNECTION)`
- Unique `storage_account_name` (3-24 lowercase alphanumerics)

### Terraform usage (local)
```bash
terraform init
terraform plan -var "resource_group_name=rg-example-123" -var "storage_account_name=stexample123456" -out tfplan
terraform apply tfplan
```

### Variables
- `resource_group_name` (required)
- `storage_account_name` (required)
- `location` (default `eastus`)

### Outputs
- `storage_account_id`
- `primary_blob_endpoint`

### Azure DevOps pipeline
See `azure-pipelines.yml`.

### Python verification
```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/verify.py --subscription-id <sub> --resource-group-name rg-example-123 --account-name stexample123456
```

