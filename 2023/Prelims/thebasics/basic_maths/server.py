#!/usr/bin/env python3
from random import randint
from Crypto.Util.number import getPrime
from sympy.ntheory.modular import crt
from sympy import lcm, gcd
import sys
sys.set_int_max_str_digits(0)

def get_int(msg):
	try:
		return int(input(msg))	
	except Exception as e:
		print("the input should be a number")
		print(e)
		exit(0)

print("Welcome to basic maths; you will be tested on some algorithms that are useful to know when solving cryptographic challenges")

print('### Problem 1/4 ###')
k = 3
mods = []
while len(set(mods)) != k:
	mods = [getPrime(10) for _ in range(k)]
mult = 1
for m in mods: mult *= m
x = (randint(0,mult))
rems = [x % m for m in mods]

print("Figure out x: that satisfies the following equations")
for m,r in zip(mods,rems):
	print(f'x = {r} mod {m}')
inp = get_int('give me x > ')

if inp == x: 
	print("correct!")
else:
	print("wrong!")
	exit(0)

print("### Problem 2/4 ###")

print("Figure out x: I'll tell you if you guessed above or below x (0 <= x <= 10000)")
from math import ceil, log2
n = 10000
x = randint(0,n)
k = ceil(log2(n)) +1
for i in range(k):
	inp = get_int(f'what is x? {i+1}/{k}> ')
	if inp < x: print('below x')
	elif inp > x: print('above x')
	else: break

if x == inp:
	print('correct!')
else:
	print("wrong!")
	exit(0)
	

print("### Problem 3/4 ###")

print("Figure out x: give me a number n, I'll tell you the lowest common multiple of x and n")
x = randint(0,10000)
n = get_int(f'give me n> ')
print(f'here is lcm(n,x): {lcm(n,x)}')
inp = get_int(f'what is x? > ')
if x == inp:
	print('correct!')
else:
	print('wrong!')
	exit(0)

print("### Problem 4/4 ###")

print("Figure out x: give me a number n, I'll tell you the greatest common divisor of x and n")

x = randint(0,10000)
n = get_int(f'give me n> ')
print(f'here is gcd(n,x): {gcd(n,x)}')
inp = get_int(f'what is x? > ')
if x == inp:
	print('correct!')
else:
	print('wrong!')
	exit(0)


print(f'here is your flag {open("flag.txt").read()}')



