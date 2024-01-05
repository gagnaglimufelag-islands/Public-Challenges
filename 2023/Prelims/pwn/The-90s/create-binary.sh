#!/bin/bash

NAME=90s
OUTPUT=chal/90-s

sudo docker build -f Dockerfile.binary -t $NAME-bin .
sudo docker run --rm $NAME-bin > $OUTPUT
chmod +x $OUTPUT
