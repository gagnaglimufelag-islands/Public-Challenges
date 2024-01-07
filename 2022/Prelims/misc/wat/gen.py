import itertools
import random

def randseq():
    while True:
        yield 0

with open('original.pdf', 'rb') as f:
    doc = f.read()

with open('wat', 'wb') as f:
    f.write(bytes(doc[::-1]))


