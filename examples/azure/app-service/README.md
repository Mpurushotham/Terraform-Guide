## Azure App Service (Linux Web App)

Creates an App Service Plan (Linux) and a Python 3.11 Web App.

### Usage
```bash
terraform init
terraform apply -auto-approve \
  -var "resource_group_name=rg-app-demo" \
  -var "app_service_plan_name=asp-demo" \
  -var "webapp_name=webapp-demo-123456"
```

Output: `default_hostname`

Pipeline and verification follow the same pattern.

