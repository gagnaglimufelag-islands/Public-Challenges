#!/usr/bin/env python2

from Crypto.Util.number import getPrime
from numpy.linalg import lstsq
from base64 import b64encode
import numpy as np

noiseSize = 22

while True:
	flag = raw_input('Enter your secret: ').strip()
	if flag[:5] == '10an{' and flag[-1] == '}':
		flag = flag[5:-1]
		break
	else:
		print 'Invalid secret (missing 10an flag wrapper)'

# initialize 
secret = np.zeros((len(flag), 1))
noise = np.zeros((noiseSize, 1))
random = np.zeros((noiseSize, len(flag)))

requiredBits = noiseSize * len(flag) * 8 - 36
p1 = getPrime(requiredBits)
p2 = getPrime(36)
p3 = p1 * p2

# print the key if the user wants it
if raw_input('Print key: (y/n)').lower() == 'y':
	print 'Your decryption key is: {}'.format(b64encode(str(p2)))
print 'Your random data is: {}'.format(b64encode(str(p3)))

# Convert prime to noise and chuck it into the noise array
for x in range(noiseSize):
	noise[x][0] = (p2 % 3) - 1
	p2 //= 3

# factoring p3 should be impossible so it should be safe to use it as random data... right?
for x in range(noiseSize):
	for y in range(len(flag)):
		random[x, y] = p3 & 0xff # exctract exactly one byte
		p3 >>= 8 # effectively the same as p3 //= 0xff

# Chuck the secret into the secret array
for x in range(len(secret)):
	secret[x][0] = ord(flag[x])


output = np.matmul(random, secret) # incorporate the secret
output = np.add(output, noise) # add the noise

output = ','.join([str(int(elem[0])) for elem in output])
output = b64encode(output)
print 'Your ciphertext is: {}'.format(output)
