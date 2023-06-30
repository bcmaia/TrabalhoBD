#!/bin/bash

python3 -m pip install --user virtualenv
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
