#!/usr/bin/env python2

from numpy.linalg import lstsq
from base64 import b64decode
from rho import pollardRho # comes from rho.py
from math import ceil
import numpy as np

randomData = 'MTgzMDg3MTAyODAwMTM4MjA5MjAxODIzMDQzNTY1MTExODg4MzkwMDEzNjA2MTAyMTM3MzQ0OTg1NzU3MDQ0OTU0OTMyNTYyMjkxMTY1NDMxODg0NzY0MjY3NDc5NzgyNDIwMDg0NzAzMTYxNTQyNjg2MTk1MDM5Nzg2MDIzMDgxMDIwNzAxNzc3ODg2NjA3NzkyNTkyNzI2NTU0NDgxNDUxMzA3NDUwMzA3MjMzNTgyNTU2NDUyNzc4MjQzMTUyMTc1NDUyODMxOTEyMjA4NDk0NzAwMTkyMzczOTM0ODkxNTM1NDQxMjM3MjU1MzQ2MTEzNTE0Nzg3NDY0NTcxNjEwMjU1MTU1NDU4NzAwNDgwMDYwODIwMTYwNzM2OTQ3MTA4NjE1MDQ4OTU0MjgxNDEzODc0MzcwNzU2MDM4NTQ4MjQ0ODQ3MDM1MDgzNjQyMjc1NTczNzYzNzk0NDM2NDc3MDM4MTUxMTE3OTUyMjE0NjE2MTI4ODU1MDg0NDQ2MTY1MTc0NjQ2ODMyMzk4NDc1Mzg1MjM4Nzg0OTgxNDk1NTEwODMzMDQ0MzUwMjQ4OTg2ODA5MjQ4MjQxNjU4MTQ4NTUyNDI1NDQ3NDg5OTE5MzM2MzI1NzEzMjYxNTc5MzQ3NTM4ODUzODEyODIzNTk5MzkyNjIwODY2MjExMjY2NTQxMzA3NDMxODQzMTk5NDY0NTA3OTYwOTYyOTc3MzU0MzEyNTMzNDUxMTAwMzQ1OTUyMDkyMjI4NjU2NDE4NzU5Mzg2MDc0NTAxNjEwMzA0NDY3NTQ2Mjg4ODY3OTk3MzI2MTUwOTgwOTQxODgwMjk3MDc0MTUzNjMwMDA5MDc3NjI4MDA0Nzc4MjgxOTE4NzczODg5NTQ4NzQyODAwMjYwMTEzMzY3NTk2MjUyMTA4MjE3Mjc1NjkwNzIxNjI0NzU3MTY4MzExMjczNjc3MzAxOTMxODM0NTgzODQwOTYyMDE0ODYyMjgzOTY4MDE2MjQ3MjIzMzAzMDQwMDEwNTM4NzMzMTM1MTE2NjI0MjQxNjg2MzUyNjQ2MjkxMDg4ODE5OTE0NTU2NzE0MjM3MjgwODAwNjM0ODc1ODg0MTk1MTU5MjcxNDQ4NjY2ODAzMjMxODc4OTMwOTc1ODMwNjYwMDAzNzAxNzIzOTYyNzg3MjkzMTUzNjU1MjEzNzEwMDA0MjAzODMzMDkwNDE5NDc0MjY2MzE3MzUzMTE5MjkyNzAxNzc1MjYyNzIwNzk3MjIzODA4MzU5'
ciphertext = 'MTg4MDE0LDE2Mzg1NywxOTkyNDMsMjIyMjE1LDIxMDg2NiwyMTMzNjIsMjA5OTc0LDE2MzY2OCwxNzc2MjIsMjI5MTIzLDIwODkwMCwxOTc1NTEsMTk0NTM1LDE5OTM2MSwxNzQ1NjMsMTgyODUyLDIzMjQyMywxMjUwMjEsMTI4MDQ0LDIwNDczNCwxNzk0ODMsMTc1NzMz'

p3 = int(b64decode(randomData))
p2 = pollardRho(p3)
p1 = p3 / p2
noiseSize = 22
flagLength = int(ceil(p3.bit_length() / float(noiseSize)) / 8)
random = np.zeros((noiseSize, flagLength))
secret = np.zeros((noiseSize, 1)) # change the name of this to ciphertextsomething
ciphertext = b64decode(ciphertext).split(',')

for x in range(noiseSize):
	secret[x][0] = int(ciphertext[x]) + (p2 % 3) - 1
	p2 //= 3

for x in range(noiseSize):
	for y in range(flagLength):
		random[x, y] = p3 & 0xff # exctract exactly one byte
		p3 >>= 8 # effectively the same as p3 //= 0xff

print random.shape, secret.shape

x = lstsq(random, secret)
print '10an{' + ''.join(map(lambda x: chr(int(round(x[0]))), x[0])) +'}'