import string
import yaml
import random

UPPER = string.ascii_uppercase
N = len(UPPER)

MESSAGE = yaml.safe_load(open('meta.yml'))['flags'][0]['flag']

def lmap(letter, shift):
    letter = letter.upper()
    if letter in UPPER:
        return UPPER[(UPPER.index(letter) + shift) % N]
    return letter

def encrypt(s, shift):
    return ''.join(map(lambda x: lmap(x, shift), s))

def main():
    s = MESSAGE.upper()
    for _ in range(100000):
        s = encrypt(s, random.randint(0,26))

    open('rshift.txt', 'w').write(s)


main()
