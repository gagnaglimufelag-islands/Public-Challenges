from Crypto.Util.number import long_to_bytes as ltb
from secrets import randbits
from hashlib import sha256
from sys import argv

def passwordBasedKeyDerivationFunction(password, iterations = 69):
	for _ in range(iterations):
		password = sha256(password + b'Watame Factory!').digest()
	
	return password

def encrypt(data, key):
	dataLen = len(data)
	keyLen = len(key)
	data = bytearray(data)
	for idx in range(dataLen):
		data[idx] ^= key[idx % keyLen]
	return data


if len(argv) != 2:
	print('Usage: ./encrypt.py FILE')
	exit(1)

password = ltb(randbits(999))[:2]

with open(argv[1], 'rb') as f:
	data = f.read()

with open(f'{argv[1]}.enc', 'wb') as f:
	key = passwordBasedKeyDerivationFunction(password)
	enc = bytes(encrypt(data, key))
	f.write(enc)
