resource "azurerm_resource_group" "this" {
  name     = var.resource_group_name
  location = var.location
  tags = {
    owner               = "example"
    environment         = "dev"
    cost_center         = "cc-0000"
    data_classification = "internal"
  }
}

