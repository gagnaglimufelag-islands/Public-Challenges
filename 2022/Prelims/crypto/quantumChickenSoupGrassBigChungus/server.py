#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from random import SystemRandom # proper randomness, not pythons shitty default random

p = 27046780809278300597
g = 2
secret = SystemRandom().randrange(p)
ciphertext = pow(g, secret, p)

print '''Hello there old fella, thanks for testing my secret encryption system. If you can find my secret I'll give you a flag, mkay?
You'll only have one chance though. Good luck!'''

print '''p: {}
g: {}
ciphertext: {}'''.format(p, g, ciphertext)

guess = raw_input()
if guess.isdigit():
	guess = int(guess)
else:
	print 'YAMETEKUDASTOP!'
	exit()

if pow(g, guess, p) != ciphertext:
	print 'lmao nope 草草草草草草草草草草草草草草草草草草草草草草草'
else:
	with open('flag.txt') as f:
		print f.read()
