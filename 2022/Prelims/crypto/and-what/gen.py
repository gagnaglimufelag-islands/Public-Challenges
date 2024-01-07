import string
import yaml
from itertools import cycle
from base64 import b64encode, b64decode

UPPER = string.ascii_uppercase
N = len(UPPER)

MESSAGE = yaml.safe_load(open('meta.yml'))['flags']
KEY = b'corr3cthors3b4tterystapl3'

def encrypt(s):
    return bytes([x & y for x,y in zip(cycle(KEY), s.encode())]), bytes([x | y for x,y in zip(cycle(KEY), s.encode())])

def main():
    aand, oor = encrypt(MESSAGE)

    with open('andor.txt', 'w') as f:
        print('AND:', b64encode(aand).decode(), file=f)
        print('OR:', b64encode(oor).decode(), file=f)

main()

def decrypt(and_part, or_part, key):
    b = []
    for a, o, k in zip(format(and_part, '08b'), format(or_part, '08b'), format(key, '08b')):
        if k == '1':
            b.append(a)
        else:
            b.append(o)
    return int(''.join(b), 2)

def decipher(and_part, or_part, key):
    return bytes(decrypt(a, o, k) for k, a, o in zip (cycle(key), and_part, or_part))


def solve():
    a, o = open('andor.txt').read().splitlines()
    a = a.split()[-1]
    o = o.split()[-1]

    and_part = b64decode(a)
    or_part = b64decode(o)

    print(decipher(and_part, or_part, KEY))

