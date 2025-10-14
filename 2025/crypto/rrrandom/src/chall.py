from Crypto.Util.number import *
import random


flag = b'gg{this_is_not_the_flag_ur_looking_for}'
flagi = bytes_to_long(flag)

p = getPrime(300)
q = getPrime(300)
n = p*q
e = 3
m = 42

print("Welcome to my random encryption service, where we encrypt random garbage for fun")
while True:
    wf = input("with flag (y/n/q)?")
    if wf == 'y':
        r = pow(2,m)*flagi + random.randint(1, pow(2,m))
    else:
        r = random.randint(1, pow(2,m+len(flag)*8))
        print(f'{r = }') # TODO: remove debugging
    if wf == 'q': break

    print(pow(r, e, n))
