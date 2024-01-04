#!/usr/bin/python3
import sys

VOWELS = ['A', 'Á', 'E', 'É', 'I', 'Í', 'O', 'Ó', 'U', 'Ú', 'Y', 'Ý', 'Æ', 'Ö']
KEY = "ub"

#e = sys.stdin.readline().strip()

s = sys.stdin.read()
e = "D" #Change to anything else for decryption
if e == "D":
    for c in s:
        if c.upper() in VOWELS:
            sys.stdout.write(KEY)
        sys.stdout.write(c)
else:
    i = 0
    while i < len(s):
        if i < len(s) - 2 and s[i].lower() == "u" and s[i+1].lower() == "b" and s[i+2].upper() in VOWELS:
            sys.stdout.write(s[i+2])
            i += 2
        else:
            sys.stdout.write(s[i])
        i += 1
