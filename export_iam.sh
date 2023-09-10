#!/bin/bash

GCLOUD_PROJECT_ID=$1
EXPORT_JSON_PATH=$2

gcloud config set project $GCLOUD_PROJECT_ID
gcloud projects get-iam-policy $GCLOUD_PROJECT_ID --format=json > $EXPORT_JSON_PATH
