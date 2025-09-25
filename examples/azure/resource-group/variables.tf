variable "location" {
  description = "Azure region for the resource group"
  type        = string
  default     = "eastus"
}

variable "resource_group_name" {
  description = "Name of the resource group to create"
  type        = string
}

