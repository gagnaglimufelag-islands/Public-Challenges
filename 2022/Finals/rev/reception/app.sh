#!/bin/bash

set -e

docker build -t reception .
docker run -it --rm -p 5000:5000 reception
