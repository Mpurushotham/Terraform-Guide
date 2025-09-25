resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_servicebus_namespace" "ns" {
  name                = var.namespace_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard"
}

resource "azurerm_servicebus_queue" "q" {
  name                = var.queue_name
  namespace_id        = azurerm_servicebus_namespace.ns.id
  enable_partitioning = true
}

