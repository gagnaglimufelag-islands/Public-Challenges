#!/bin/sh

openssl rsautl -decrypt -in flag.enc -inkey key.pem
