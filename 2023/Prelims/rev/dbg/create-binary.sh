#!/bin/bash

NAME=dbg
OUTPUT=chal/dbg

sudo docker build -f Dockerfile.binary -t $NAME-bin .
sudo docker run --rm $NAME-bin > $OUTPUT
chmod +x $OUTPUT
