#!/bin/bash

set -e

rm -rf ./bin/diagon_alley
docker build -t diagon_alley .
docker run --rm -v "$(pwd)"/bin:/app/bin --name diagon_alley diagon_alley
