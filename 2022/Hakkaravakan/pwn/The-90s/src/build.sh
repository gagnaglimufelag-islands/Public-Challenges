#!/bin/bash
gcc -fno-stack-protector -m32 -z norelro -z execstack -no-pie -o 90-s chal.c
