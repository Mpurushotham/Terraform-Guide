## Azure Virtual Network + Subnet

Creates a VNet and a subnet.

### Usage
```bash
terraform init
terraform apply -auto-approve \
  -var "resource_group_name=rg-vnet-demo" \
  -var "vnet_name=vnet-demo"
```

Outputs: `vnet_id`, `subnet_id`.

Pipeline and verification follow the same pattern as other examples.

