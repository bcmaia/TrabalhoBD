#!/bin/bash

python -m pip install venv
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
