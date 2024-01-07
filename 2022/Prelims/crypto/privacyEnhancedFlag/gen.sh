#!/bin/sh

openssl genrsa -out key.pem 4096
openssl rsautl -encrypt -in flag.txt -inkey key.pem -out flag.enc
