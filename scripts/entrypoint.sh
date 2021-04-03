#!/bin/bash

set -e

PORT="${PORT:-3333}"

for arg in "$@"
do
    mode=$arg
done

if [ "$mode" = "prod" ]
then
	WORKER_CLASS="uvicorn.workers.UvicornWorker"
	APP_MODULE="app.main"
	GUNICORN_CONF="config/gunicorn.py"
	VARIABLE_NAME="app"

    exec gunicorn \
    	--worker-class="$WORKER_CLASS" \
    	--config="$GUNICORN_CONF" \
    	"${APP_MODULE}:${VARIABLE_NAME}"

elif [ "$mode" = "dev" ]
then
    uvicorn app.main:app --reload --host "0.0.0.0" --port "$PORT"

else
    echo "Unknown mode '$mode'"
    exit 1
fi
