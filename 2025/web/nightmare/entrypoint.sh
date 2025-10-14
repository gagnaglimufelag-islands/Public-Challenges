#!/bin/bash
set -e
nginx
exec su -s /bin/bash nginx -c "python3 /src/app.py"

