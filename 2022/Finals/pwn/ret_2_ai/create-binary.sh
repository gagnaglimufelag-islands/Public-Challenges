#!/bin/bash

sudo docker build -f Dockerfile.binary -t ai-bin .
sudo docker run --rm ai-bin > ai
chmod +x ai
