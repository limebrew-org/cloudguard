#!/bin/bash

#? virtaul environment name
ENV_NAME="cloudguard"

#? Activate environment
source ~/miniconda3/bin/activate $ENV_NAME

#? Build package
poetry build