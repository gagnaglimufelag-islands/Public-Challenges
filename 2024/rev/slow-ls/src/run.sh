#!/bin/bash

docker build -t 'builder' .
docker run -v ./build-output:/build 'builder'