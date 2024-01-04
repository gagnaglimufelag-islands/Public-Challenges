from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import time
import z3
import random
random.seed(133337)

p = getPrime(1024)
q = getPrime(1024)
e = 0x10001

with open('flag.txt', 'rb') as f:
    flag = bytes_to_long(f.read())


n = p*q

print(n)

p_bin = bin(p)[2:].zfill(1024)
out_p = ''
c = 0
for b in p_bin:
    if not random.randint(0, 1):
        c += 1
        out_p += '?'
    else:
        out_p += b
print(out_p)

q_bin = bin(q)[2:].zfill(1024)
out_q = ''
for b in q_bin:
    if not random.randint(0, 1):
        c += 1
        out_q += '?'
    else:
        out_q += b
print(out_q)

print(long_to_bytes(pow(flag, e, n)).hex())
