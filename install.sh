#!/bin/bash

PY_VERSION="3.11"

#? virtaul environment name
ENV_NAME="cloudguardian"

#? Create environment
conda create -n $ENV_NAME python=$PY_VERSION -y

#? Activate environment
source ~/miniconda3/bin/activate $ENV_NAME

#? Install dependencies
pip install -r requirements.txt