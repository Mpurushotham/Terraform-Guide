## Azure Key Vault (Terraform + Azure DevOps + Python Verify)

Creates a Key Vault with RBAC authorization and purge protection.

### Usage
```bash
terraform init
terraform apply -auto-approve \
  -var "resource_group_name=rg-kv-demo" \
  -var "key_vault_name=kv-demo-123456"
```

### Variables
- `resource_group_name` (required)
- `key_vault_name` (required, globally unique)
- `location` (default `eastus`)
- `sku_name` (default `standard`)

### Outputs
- `vault_uri`

### Azure DevOps pipeline
See `azure-pipelines.yml`.

### Python verification
```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/verify.py --subscription-id <sub> --resource-group-name rg-kv-demo --vault-name kv-demo-123456
```

