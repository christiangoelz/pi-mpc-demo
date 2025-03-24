#!/bin/bash

sudo apt-get update
sudo apt-get install vim netcat-openbsd python3 python3-pip -y

python3 -m venv ./venv
source ./venv/bin/activate

pip install -e .

FDRSC_PATH=/home/christian/bob/third_party/federatedsecure
echo "export PYTHONPATH=${FDRSC_PATH}/client-python/src:${FDRSC_PATH}/server/src:${FDRSC_PATH}/service-simon/src:\$PYTHONPATH" >> ./venv/bin/activate
