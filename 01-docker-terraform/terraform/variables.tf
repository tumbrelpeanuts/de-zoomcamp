variable "project" {
  description = "Project"
  type        = string
  default     = "dtc-de-course-488621"
}


variable "location" {
  description = "Project Location"
  type        = string
  default     = "US"
}


variable "region" {
  description = "Project Region"
  type        = string
  default     = "us-west2"
}


variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  type        = string
  default     = "demo_dataset"
}


variable "gcs_bucket_name" {
  description = "My storage bucket name"
  type        = string
  default     = "dtc-de-course-488621-terra-bucket"
}


variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}