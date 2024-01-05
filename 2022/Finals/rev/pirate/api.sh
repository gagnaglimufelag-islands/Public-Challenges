#!/bin/bash

set -e

docker build -t api .
docker run -it --rm -p 5000:5000 api

