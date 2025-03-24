#!/bin/bash
source /home/christian/alice/venv/bin/activate
FDRSC_PATH=/home/christian/alice/third_party/federatedsecure
export PYTHONPATH=${FDRSC_PATH}/client-python/src:${FDRSC_PATH}/server/src:${FDRSC_PATH}/service-simon/src
cd /home/christian/alice/ || exit
python "app.py"