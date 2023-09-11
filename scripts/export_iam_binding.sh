#!/bin/bash

#? gcloud args
GCLOUD_PROJECT_ID=$1
GCLOUD_SERVICE_ACCOUNT_ID=$2
GCLOUD_JSON_PATH=$3
EXPORT_JSON_PATH=$4

#? Authentication
gcloud auth activate-service-account $GCLOUD_SERVICE_ACCOUNT_ID --key-file $GCLOUD_JSON_PATH
gcloud config set project $GCLOUD_PROJECT_ID

#? Export IAM policy bindings
gcloud projects get-iam-policy $GCLOUD_PROJECT_ID --format=json > $EXPORT_JSON_PATH
