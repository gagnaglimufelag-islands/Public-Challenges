#!/bin/bash

set -e

# docker stop arr
rm -rf ./bin/arr
docker build -t arr .
docker run --rm -v "$(pwd)"/bin:/app/bin --name arr arr
