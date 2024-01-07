#!/usr/bin/env python2

from pwn import xor
from os import urandom

with open('flag.png') as f:
	image = f.read()

OTP = urandom(16)
image = xor(OTP, image)

with open('flag.png.enc', 'w') as f:
	f.write(image)
