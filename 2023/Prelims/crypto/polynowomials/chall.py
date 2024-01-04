from polynomial import *
from random import sample
from time import sleep

alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?_{}'
header = r"""              _                                          _       _
             | |                                        (_)     | |
  _ __   ___ | |_   _ _ __   _____      _____  _ __ ___  _  __ _| |___
 | '_ \ / _ \| | | | | '_ \ / _ \ \ /\ / / _ \| '_ ` _ \| |/ _` | / __|
 | |_) | (_) | | |_| | | | | (_) \ V  V / (_) | | | | | | | (_| | \__ \
 | .__/ \___/|_|\__, |_| |_|\___/ \_/\_/ \___/|_| |_| |_|_|\__,_|_|___/
 | |             __/ |
 |_|            |___/                                                  """



def randomPolynomial():
	res = Polynomial([1])
	roots = sample(alphabet, len(alphabet) >> 1)
	for root in map(ord, roots):
		res *= Polynomial([-root, 1])
	return res

with open('flag.txt') as f:
	FLAG = f.read()

print(header)
print("""Welcome to polynowomials. The home of polynomials, flags and absurdists.
What would you like to do?""")
while True:
	print("""
a) Contemplate life.
b) Generate a random polynomial
c) Get flag
q) Quit.""")
	ans = input().lower()
	if ans[0] == 'a':
		print('Contemplating...')
		sleep(2)
	elif ans[0] == 'b':
		print(f'{randomPolynomial()}')
	elif ans[0] == 'c':
		try:
			index = int(input('Flag index: '))
		except:
			raise Exception('Lmao not a chance')
		if index < 0 or index >= 69:
			raise Exception('Lmao not a chance')
		char = ord(FLAG[index])
		polynowomial = randomPolynomial() * Polynomial([-char, 1])
		print(polynowomial)
	else:
		print('Ok byeeeeee')
		exit(0)
