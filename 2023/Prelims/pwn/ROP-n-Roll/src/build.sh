#!/bin/bash

gcc -fno-stack-protector -no-pie -m32 -z norelro -o chal chal.c funcs.h
