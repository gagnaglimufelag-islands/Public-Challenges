from Crypto.Util.number import *
import random

flag = b'gg{fake_flag}'

p = getPrime(1024)
q = getPrime(1024)
n = p*q
d = getPrime(16)

phi = (p-1)*(q-1)
e = pow(d,-1,phi)

l = 1024*2 - len(flag)*8 
padded = bytes_to_long(flag)*pow(2,l) + random.getrandbits(l)

print(f'{n = }')
print(f'{e = }')
print('enc =', pow(padded, e, n))
