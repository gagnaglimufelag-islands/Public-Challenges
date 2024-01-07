from binascii import hexlify, unhexlify
from itertools import zip_longest
import yaml

meta = yaml.safe_load(open('meta.yml'))

flag = meta['flags']

UP = '👍'
DOWN = '👎'

curr = flag.encode()
for _ in range(10):
    curr = hexlify(curr)

binary = ''.join([bin(byte)[2:].rjust(8, '0') for byte in curr])
final = binary.replace('1', UP).replace('0', DOWN)
with open('thumbs.txt', 'w') as f:
    f.write(final)


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def solve():
    t = open('thumbs.txt').read()
    bts = [int(''.join(g).replace(UP, '1').replace(DOWN, '0'), 2) for g in grouper(t, 8)]
    data = bytes(bts)
    while True:
        try:
            data = unhexlify(data)
        except:
            return data

