terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}

  subscription_id = "b4ef7551-a92d-463d-b63c-149ac66efad0"
  client_id       = "b71b9374-6f24-4ade-b593-1ac3a86a7957"
  client_secret   = "xeK8Q~.UZAUzaYYx-gFnt5OQxchGA1IgOSvLwcxJ"
  tenant_id       = "1850beb1-e58a-4c4e-9f03-2e18987a59fb"
}
