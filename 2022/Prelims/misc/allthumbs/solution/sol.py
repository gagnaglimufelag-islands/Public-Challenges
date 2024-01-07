import sys
from binascii import unhexlify
from itertools import zip_longest

UP = '👍'
DOWN = '👎'

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

filename = sys.argv[1]
t = open(filename).read()
bts = [int(''.join(g).replace(UP, '1').replace(DOWN, '0'), 2) for g in grouper(t, 8)]
data = bytes(bts)
while True:
    try:
        data = unhexlify(data)
    except:
        print(data)

