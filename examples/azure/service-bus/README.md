## Azure Service Bus (Namespace + Queue)

Creates a Standard Service Bus namespace and queue.

### Usage
```bash
terraform init
terraform apply -auto-approve \
  -var "resource_group_name=rg-sb-demo" \
  -var "namespace_name=sb-demo-123456"
```

Outputs: `namespace_id`, `queue_id`.

Pipeline and verification follow the same pattern.

