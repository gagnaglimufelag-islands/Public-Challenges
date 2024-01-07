#!/usr/bin/env python3

from Crypto.Util.number import getPrime, bytes_to_long as btl
from hashlib import sha512

bitlength = 1024
p = getPrime(bitlength)
FLAGTEXT = btl(b'A Lattice is post-quantum protocol\'s worst friend gg{whyDoTheyCallItOvenWhenYouOfInTheColdFoodOfOutHotEatTheFood?_5238f72133}')

print(f'p: {p}')

while True:
	x = input('x: ').encode()
	x = pow(2, btl(sha512(x).digest()), p)
	res = FLAGTEXT * x
	res %= p
	res = res >> (bitlength - 48)
	print(f'res: {res}')
