## Azure SQL Database

Creates an Azure SQL Server and a Basic-tier database.

### Usage
```bash
terraform init
terraform apply -auto-approve \
  -var "resource_group_name=rg-sql-demo" \
  -var "sql_server_name=sql-demo-123456" \
  -var "sql_admin_login=sqladmin" \
  -var "sql_admin_password=ChangeMe123!" \
  -var "sql_database_name=dbdemo"
```

Outputs: `sql_server_fqdn`, `database_id`.

Pipeline and verification follow the same pattern.

