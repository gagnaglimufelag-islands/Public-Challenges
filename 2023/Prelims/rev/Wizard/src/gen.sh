#!/bin/bash

apt-get update && apt-get install -y build-essential upx
gcc -static -Wall -o w1zArD wizard.c
upx -9 w1zArD
