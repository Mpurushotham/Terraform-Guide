## Examples and Usage Instructions

This repository does not include modules yet; the examples below demonstrate how consumers should use standardized modules.

### Minimal Consumption Example (Local Path)

```hcl
terraform {
  backend "s3" {}
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

module "network" {
  source = "../modules/network"

  vpc_cidr       = "10.0.0.0/16"
  allowed_cidrs  = ["10.0.0.0/8"]
  environment    = var.environment
  owner          = var.owner
  cost_center    = var.cost_center
  data_classification = var.data_classification
}

variable "region" {}
variable "environment" {}
variable "owner" {}
variable "cost_center" {}
variable "data_classification" {}
```

### Registry Module Example

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "example-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true

  tags = {
    owner              = var.owner
    environment        = var.environment
    cost_center        = var.cost_center
    data_classification = var.data_classification
  }
}
```

### tfvars and Commands

`terraform.tfvars` example:

```hcl
region = "us-east-1"
environment = "staging"
owner = "platform-team"
cost_center = "cc-1234"
data_classification = "internal"
```

Commands:

```bash
terraform init
terraform fmt -check
terraform validate
terraform plan -out tfplan
terraform apply tfplan
```

### Workspaces

Use Terraform workspaces or separate state backends per environment. Do not share state across environments.

