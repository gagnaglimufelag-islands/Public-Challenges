from Crypto.Util.number import getPrime, bytes_to_long as btl, long_to_bytes as ltb
from hashlib import sha512
from tqdm import trange
from pwn import *
from time import time

if args['NOSPAMPLOX']:
	NOSPAMPLOX = True
else:
	NOSPAMPLOX = False

n = 1024
MSBs = 48
shiftAmt = n - MSBs
k = MSBs - 2
# NOTE: The attacker has an advantage when k \approx sqrt(log_2 p) and d = 2 * sqrt(log_2 p)
# d = 64
d = 23

if args['LOCAL']:
	conn = process('./serverUncensored.py')
else:
	domain = args['DOMAIN']
	port = int(args['PORT'])
	conn = remote(domain, port)

p = int(conn.readline()[3:])
inputs = []
leaks = []

for x in trange(d):
	x = str(x).encode()
	conn.sendline(x)
	inputs.append(pow(2, btl(sha512(x).digest()), p))
	leaks.append(int(conn.recvline()[7:]) << shiftAmt)

conn.close()

print(f'Bits in p: {n}')
print(f'Queries: {d}')
print(f'MSBs: {k+2}')

def buildBasis(oracleInputs):
	"""Returns a basis using the HNP game parameters and inputs to our oracle
	"""
	basisVectors = []
	for i in range(d):
		pVector = [0] * (d+1)
		pVector[i] = p
		basisVectors.append(pVector)
	basisVectors.append(list(oracleInputs) + [QQ(1)/QQ(p)])
	return Matrix(QQ, basisVectors)

def approximateClosestVector(basis, v):
	"""Returns an approximate CVP solution using Babai's nearest plane algorithm.
	"""
	BL = basis.LLL()
	G, _ = BL.gram_schmidt()
	_, n = BL.dimensions()
	small = vector(ZZ, v)
	for i in reversed(range(n)):
		c = QQ(small * G[i]) / QQ(G[i] * G[i])
		c = c.round()
		small -= BL[i] * c
	return (v - small).coefficients()

print('Building lattice')
# Build a basis using our oracle inputs
lattice = buildBasis(inputs)

if NOSPAMPLOX:
	print("Solving CVP using lattice with basis: [...]")
else:
	print("Solving CVP using lattice with basis:\n%s\n" % str(lattice))

# The non-lattice vector based on the oracle's answers
u = vector(ZZ, list(leaks) + [0])
if NOSPAMPLOX:
	print("Vector of MSB oracle answers: [...]")
else:
	print("Vector of MSB oracle answers:\n%s\n" % str(u))

# Solve an approximate CVP to find a vector v which is likely to reveal alpha.
d = time()
v = approximateClosestVector(lattice, u)
print(f'CVP took {time()-d}s')
if NOSPAMPLOX:
	print("Closest lattice vector: [...]")
else:
	print("Closest lattice vector:\n%s\n" % str(v))

recoveredAlpha = (v[-1] * p) % p
print(f'FLAG: {ltb(recoveredAlpha)}')
