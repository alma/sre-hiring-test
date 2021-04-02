#!/bin/bash

set -e

PORT="${PORT:-3333}"

for arg in "$@"
do
    mode=$arg
done

if [ "$mode" = "prod" ]
then
    # Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
    # And then will start Gunicorn with Uvicorn
    source /start.sh

elif [ "$mode" = "dev" ]
then
    uvicorn app.main:app --reload --host "0.0.0.0" --port "$PORT"

else
    echo "Unknown mode '$mode'"
    exit 1
fi
