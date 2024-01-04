import hashlib
from tqdm import trange
from base64 import b64decode as b64d
from ed25519 import SigningKey
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl

# with open('test2.id_ed25519') as f:
with open('censored.id_ed25519') as f:
	data = ''.join(f.read().split('\n')[1:-1])
	data = b64d(data)

pkPosition = 0x7d
pkLen = 0x20
pk = data[pkPosition:pkPosition + pkLen]
print 'public key: {}'.format(pk.encode('hex'))

skPosition = 0xa1
skLen = 0x20
origSk = data[skPosition:skPosition + skLen]
origSk = btl(origSk)
print 'partial secret key: {}'.format(hex(origSk)[2:])

origSk &= 0x00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff


for hidden in trange(0x100000):
	sk = origSk
	sk |= hidden << 236
	sk = ltb(sk).rjust(32, '\x00')
	maybePk = SigningKey(sk)
	if maybePk.vk_s == pk:
		print '===== Seed Found ====='
		print sk.encode('hex')
		break
