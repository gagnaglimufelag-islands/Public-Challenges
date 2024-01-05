#!/bin/bash

CHAL=ret2win

sudo docker build -f Dockerfile.binary -t $CHAL-bin .
sudo docker run --rm $CHAL-bin > chal
chmod +x chal
