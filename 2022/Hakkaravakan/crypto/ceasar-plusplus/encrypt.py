#!/bin/python3
import string
alph = string.ascii_lowercase
flag = input()

ceaser = 12

enc = ''
for i, f in enumerate(flag):
    if f in alph:
        enc += alph[(alph.index(f)+ceaser+i)%len(alph)]
    else: enc += f
print(f'{enc}')

