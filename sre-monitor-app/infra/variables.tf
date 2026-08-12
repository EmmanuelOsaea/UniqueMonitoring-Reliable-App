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
description = " "
default = " "
