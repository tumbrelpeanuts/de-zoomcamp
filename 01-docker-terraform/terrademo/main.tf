terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
# Credentials only needs to be set if you do not have the GOOGLE_APPLICATION_CREDENTIALS set
#  credentials = "./keys/my-creds.json"
  project = "dtc-de-course-507019"
  region  = "us-west2"
}

resource "google_storage_bucket" "demo-bucket" { # "demo-bucket ": variable name that is local
  name          = "dtc-de-course-507019-terra-bucket" # name has to be globally unique to all GCP
  # can use project-id + bucket
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1 # Minimum age of an object in days to satisfy this condition. Default is 0.
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}