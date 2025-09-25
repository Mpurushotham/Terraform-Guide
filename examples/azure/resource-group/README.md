## Azure Resource Group (Terraform + Azure DevOps + Python Verify)

### What this example does
Creates a single Azure Resource Group using Terraform, validates in Azure DevOps, and verifies existence with a Python script.

### Prerequisites
- Azure subscription and permissions to create resource groups
- Azure DevOps Service Connection (ARM) named `$(AZURE_SERVICE_CONNECTION)`
- Azure DevOps variable `RESOURCE_GROUP_NAME` set to a globally unique name

### Terraform usage (local)
```bash
terraform init
terraform plan -var "resource_group_name=rg-example-123" -out tfplan
terraform apply tfplan
```

### Variables
- `resource_group_name` (string, required)
- `location` (string, default `eastus`)

### Outputs
- `resource_group_id`
- `resource_group_name`

### Azure DevOps pipeline
See `azure-pipelines.yml`. It runs validate/plan on PR, and manual apply on main.

### Python verification
Install deps and run:
```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/verify.py --subscription-id <sub> --resource-group-name <name>
```

