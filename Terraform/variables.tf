variable "environment_variables_sql" {
  type = map(string)
  default = {
    "ACCEPT_EULA"       = "Y"
    "MSSQL_SA_PASSWORD" = "liam-logan@lloyds2022"
  }
}
