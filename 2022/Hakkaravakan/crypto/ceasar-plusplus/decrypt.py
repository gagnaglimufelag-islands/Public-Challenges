#!/bin/python3
import string
alph = string.ascii_lowercase
enc = input()
for ceaser in range(len(alph)):
    flag = ''
    for i,f in enumerate(enc):
        if f in alph:
            flag += alph[(alph.index(f)-ceaser-i)%len(alph)]
        else: flag += f
    if flag.startswith('boo{'):
        print(f'{flag = }')
