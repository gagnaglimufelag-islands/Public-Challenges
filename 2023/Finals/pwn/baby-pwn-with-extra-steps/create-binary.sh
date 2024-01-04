#!/bin/bash

NAME=baby-pwn-with-extra-steps
OUTPUT=src/chall

sudo docker build -f Dockerfile.binary -t $NAME-bin .
sudo docker run --rm $NAME-bin > $OUTPUT
chmod +x $OUTPUT
