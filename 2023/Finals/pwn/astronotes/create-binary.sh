#!/bin/bash

NAME=astronotes
OUTPUT=src/chal

sudo docker build -f Dockerfile.binary -t $NAME-bin .
sudo docker run --rm $NAME-bin > $OUTPUT
chmod +x $OUTPUT
