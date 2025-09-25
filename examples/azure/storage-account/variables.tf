variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "resource_group_name" {
  description = "Existing or new RG name"
  type        = string
}

variable "storage_account_name" {
  description = "Globally unique storage account name (3-24 lowercase alphanumerics)"
  type        = string
}

