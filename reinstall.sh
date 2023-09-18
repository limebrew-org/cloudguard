#!/bin/bash

PY_VERSION="3.11.5"
POETRY_VERSION="1.4.2"

#? virtaul environment name
ENV_NAME="cloudguard"

#? Deactivate environment
source ~/miniconda3/bin/deactivate

#? Remove environment
conda env remove -n $ENV_NAME

#? Create environment
conda create -n $ENV_NAME python=$PY_VERSION -y

#? Activate environment
source ~/miniconda3/bin/activate $ENV_NAME

#? Install Poetry
pip install poetry==$POETRY_VERSION

#? Install the project dependencies
poetry install