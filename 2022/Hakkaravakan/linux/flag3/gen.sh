#!/bin/bash

sudo docker build . -t flag3
sudo docker run --mount type=bind,source=$(pwd)/setup,target=/src/out --rm flag3
