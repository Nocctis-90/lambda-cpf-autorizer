variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1" # Defina a região desejada
}

variable "TF_LAMBDA_ZIP_PATH" {
  type = string
}