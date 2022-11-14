resource "azurerm_resource_group" "lbg-hackathon" {
  name     = "lbg-hackathon"
  location = "West Europe"
}

resource "azurerm_container_registry" "acr" {
  name                = "lbghackathoncontainerregistry"
  resource_group_name = azurerm_resource_group.lbg-hackathon.name
  location            = azurerm_resource_group.lbg-hackathon.location
  sku                 = "Basic"
  admin_enabled       = false
}

resource "null_resource" "docker_push" {
  provisioner "local-exec" {
    command = <<-EOT
        docker login ${azurerm_container_registry.acr.login_server} 
        docker push ${azurerm_container_registry.acr.login_server}
      EOT
  }
}

resource "azurerm_container_group" "lbg-aci" {
  name                = "lbghackathoncontainer"
  location            = azurerm_resource_group.lbg-hackathon.location
  resource_group_name = azurerm_resource_group.lbg-hackathon.name
  ip_address_type     = "Public"
  dns_name_label      = "aci-lbg-test"
  os_type             = "Linux"
  restart_policy      = "Never"

  container {
    name   = "hello-world"
    image  = "mcr.microsoft.com/azuredocs/aci-helloworld:latest"
    cpu    = "0.5"
    memory = "1.5"


    ports {
      port     = 80
      protocol = "TCP"
    }
  }

  container {
    name   = "sql-server"
    image  = "mcr.microsoft.com/mssql/server:2019-latest"
    cpu    = "0.5"
    memory = "2"

    ports {
      port     = 1433
      protocol = "TCP"
    }

    environment_variables = var.environment_variables_sql
  }
}
