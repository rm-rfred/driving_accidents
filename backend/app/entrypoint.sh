#!/bin/sh
exec gunicorn --bind 0.0.0.0:8001 main:app -k uvicorn.workers.UvicornWorker