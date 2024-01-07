#!/usr/bin/env python2

from Crypto.Util.number import bytes_to_long
from Crypto.PublicKey import RSA

e = 3
flag = bytes_to_long('Hey, Heres my precious flag. Take good care of it, it is very valuable. gg{H4sTad_s3Nds_h1S_r3g4RDs!}')
K0 = RSA.generate(2048, e = 3)
K1 = RSA.generate(2048, e = 3)
K2 = RSA.generate(2048, e = 3)

ct0 = pow(flag, e, K0.n)
ct1 = pow(flag, e, K1.n)
ct2 = pow(flag, e, K2.n)

assert flag**e > K0.n # makes sure that the challenge cant be solved with a simple cbrt
assert flag**e > K1.n
assert flag**e > K2.n

with open('broadcast.txt', 'w') as f:
	f.write('n: {}\ne: {}\nct: {}\n\n'.format(K0.n, e, ct0))
	f.write('n: {}\ne: {}\nct: {}\n\n'.format(K1.n, e, ct1))
	f.write('n: {}\ne: {}\nct: {}\n\n'.format(K2.n, e, ct2))
