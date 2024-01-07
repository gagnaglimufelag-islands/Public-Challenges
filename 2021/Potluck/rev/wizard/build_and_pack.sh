#!/bin/sh

sudo apt update
sudo apt install build-essential -y
sudo apt install upx -y
gcc -static -Wall -o w1zArD wizard.c
upx -9 w1zArD
