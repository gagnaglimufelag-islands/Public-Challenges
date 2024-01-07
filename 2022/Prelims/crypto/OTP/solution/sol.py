#!/usr/bin/env python2

from pwn import xor

pngHeader = '89504e470d0a1a0a0000000d49484452'.decode('hex')

with open('flag.png.enc') as f:
	ciphertext = f.read()

key = xor(pngHeader, ciphertext[:16])
image = xor(key, ciphertext)
with open('res.png', 'w') as f:
	f.write(image)
