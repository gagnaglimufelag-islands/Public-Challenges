#!/usr/bin/env python2

import sys
from io import BytesIO
from struct import unpack
from base64 import b64decode as b64d

p = 0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffed
a = 0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffec
d = 0x52036cee2b6ffe738cc740797779e89800700a4d4141d8ab75eb4dca135978a3

with open('id_ed25519') as f:
	PEM = f.read().strip()

def readLength(buf):
	lengthStr = buf.read(4)
	# print lengthStr.encode('hex')
	length = unpack('>I', lengthStr)[0]
	# print length
	if length == 0:
		# raise NotImplementedError
		return 4 # this could create some confusion
	return length

PEM = PEM.split('\n')
header = PEM[0]
data = b64d(''.join(PEM[1:-1]))
footer = PEM[-1]
print 'blob length: {}'.format(len(data))

authMagic, _, data = data.partition('\x00')
print 'AUTH_MAGIC: {}'.format(authMagic)
if authMagic != 'openssh-key-v1':
	sys.stderr.write('Warning: unknown AUTH_MAGIC\n')

buf = BytesIO(data)

length = readLength(buf)
ciphername = buf.read(length)
print 'ciphername: {} (len: {})'.format(ciphername, length)

length = readLength(buf)
kdfname = buf.read(length)
print 'kdfname: {} (len: {})'.format(kdfname, length)

length = readLength(buf)
if length != 4:
	kdfOptions = buf.read(length).encode('hex')
	print 'kdfOptions: {} (len: {})'.format(kdfOptions, length)
else:
	print 'kdfOptions: None (len: 0)'

keys = readLength(buf)
print 'keys: {} (should be hardcoded to 1)'.format(keys)
if keys != 1:
	raise NotImplementedError('This parser does not support multiple keys')

print '===== Entering sshpub ====='
length = readLength(buf)
print 'sshpub length: {}'.format(length)

length = readLength(buf)
keytype = buf.read(length)
print 'keytype: {} (len: {})'.format(keytype, length)
if keytype != 'ssh-ed25519':
	sys.stderr.write('Warning: keytype {} is not supported. Expect parsing failures\n'.format(keytype))

length = readLength(buf)
pub0 = buf.read(length).encode('hex')
print 'pub0: {} (len: {})'.format(pub0, length)

print '===== Exiting sshpub ====='
print '===== Entering sshpriv ====='

length = readLength(buf)
print 'sshpriv length: {}'.format(length)

checkInt0 = buf.read(4)
print 'checkInt0: {}'.format(checkInt0.encode('hex'))
checkInt1 = buf.read(4)
print 'checkInt1: {}'.format(checkInt1.encode('hex'))

length = readLength(buf)
keytype = buf.read(length)
print 'keytype: {} (len: {})'.format(keytype, length)
if keytype != 'ssh-ed25519':
	sys.stderr.write('Warning: keytype {} is not supported. Expect parsing failures\n'.format(keytype))

length = readLength(buf)
pub0 = buf.read(length).encode('hex')
print 'pub0: {} (len: {})'.format(pub0, length)

length = readLength(buf)
priv0 = buf.read(length).encode('hex')
print 'priv0: {} (len: {})'.format(priv0, length)
privateKey = priv0[:64]
if keytype == 'ssh-ed25519':
	print 'public key: 0x{}'.format(pub0)
	# check if public key is on curve
	# TODO
	print 'private key: 0x{}'.format(privateKey)
	# check clamping
	sk = int(privateKey, 16)
	skValid = True
	# print privateKey[62:64]
	# print bin(sk & 0xff)[2:].zfill(8)
	# NOTE: not even valid since sk is actually the seed
	# NOTE: actually idk
	# if (sk >> 248) & 0x3 != 0:
	# 	skValid = False
	# 	print('clamp 0 invalid')
		# print(bin(sk & 0b11)[2:])
	# if sk & (0x80 << 31) != 0:
	# 	skValid = False
	# 	print('clamp 1 invalid')
	# if sk & (40 << 31) == 0:
	# 	skValid = False
	# 	print('clamp 2 invalid')
	# if skValid:
	# 	print('Private key has valid form')
	# else:
	# 	print('Invalid private key')

length = readLength(buf)
comment = buf.read(length)
print 'comment: {} (len: {})'.format(comment, length)

print '===== Exiting sshpriv ====='
