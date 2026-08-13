# 1. Environment & Project Metadat
var "project_name" {
type = string
description = "The prefix used for all infrastructure resource names"
default = "monitor-app"
}

var "environment" {
type = string
description = "The deployment stage(e.g., dev, staging, prod)"
default = "dev"
}

# 2. Cloud Provider Configurations
variable = "aws_region" {
type = string
description = "The deployment stage(e.g., dev, staging, prod)"
default = "dev"
}

# 3. Compute / Instance Configurations
variable = "instance_type" {
type = string
description = "The size of virtual machine instance"
default = "t3.micro"
}

# 4.Network Configurations
variable = "vpc_cidr" {
type = string
description = "The size of virtual machine instance"
default = "10.0.0.0/16"
}

# 5.Sensitive Variables(No defaults for security)
variable "db_password" {
type = string
description = "The master password  for the database layer"
sensitive = "true"
}

