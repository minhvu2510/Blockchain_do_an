#!/bin/bash

set -e

exec /usr/local/bin/gunicorn \
    --bind 0.0.0.0:${API_PORT} \
    --workers 3 \
    --timeout 120 \
    --threads 20 \
    --error-logfile - \
    --access-logfile /log/gunicorn_access.log \
    --access-logformat '%(h)s %(t)s %({Host}i)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' \
    run:APP
