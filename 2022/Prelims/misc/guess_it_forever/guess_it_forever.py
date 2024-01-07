#!/usr/bin/python2.7
from random import randint

def menu():
	print("Options")
	print("1. Guess the flag")
	print("2. Get a random number")
	print("3. quit")

FLAG = open("flag.txt", "r").read()
MAX = 10**12

i = 0
while i < 500:
	menu()
	try:
		opt = int(input("> "))
		if opt == 1:
			guess = int(input("What is the number: "))
			num = randint(1, MAX)
			if guess == num:
				print("Here is your flag %s" % FLAG)
				quit()
			else:
				print("Incorrect")
		elif opt == 2:
			print("Here is a random number %d" % randint(1, MAX))
		elif opt == 3:
			print("Goodbye")
			quit()
		else:
			print("That is not an option")
			i -= 1
		i += 1

	except (TypeError, NameError) as e:
		print("Why error")
