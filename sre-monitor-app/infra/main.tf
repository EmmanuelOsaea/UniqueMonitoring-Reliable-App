Configures the Azure Infrastructure to host your app container

provider "azurerm" {
   features {}
}

resources "azurerm_resource_group" "sre_rg" {
name = "sre-detector-resources"
location = West Canada
}

resource "azurerm_kubernetes_cluster" "aks" {
name = "sre-monitor-aks"
location = azurerm_resource_group.sre_rg.location
resource_group_name = azurerm_resource_group.sre_rg.name
dns_prefix = "sredetector"

default_node_pool {
name = "default"
node_count = 2
vm_size = "Standard_D2s_v3"

}

identity {
  type = "SystemAssigned"
}
}
