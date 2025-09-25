variable "location" { type = string, default = "eastus" }
variable "resource_group_name" { type = string }
variable "vnet_name" { type = string }
variable "address_space" { type = list(string), default = ["10.10.0.0/16"] }

