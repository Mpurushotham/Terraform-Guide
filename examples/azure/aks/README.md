## Azure Kubernetes Service (AKS)

Creates a small AKS cluster for demo/testing.

### Usage
```bash
terraform init
terraform apply -auto-approve \
  -var "resource_group_name=rg-aks-demo" \
  -var "aks_name=aks-demo-001"
```

Retrieve kubeconfig:
```bash
terraform output -raw kube_config > kubeconfig
KUBECONFIG=./kubeconfig kubectl get nodes
```

Pipeline: see `azure-pipelines.yml` for validate/plan/apply on Azure DevOps.

