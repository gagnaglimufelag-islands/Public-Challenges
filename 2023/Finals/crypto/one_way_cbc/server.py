#!/bin/python3
from hashlib import sha256
from os import urandom

key = urandom(16)
iv = urandom(16)

def xor(x,y):
    return bytes([a^b for a,b in zip(x,y)])
def hash_with_key(msg: bytes):
    return sha256(msg+key).digest()[:16]
def pad(msg: bytes):
    if len(msg) % 16 == 0: padding_len = 16
    else: padding_len = -len(msg)%16
    return msg + bytes([padding_len])*padding_len

with open('flag.txt','rb') as f:
    flag = f.read().strip()

enc = iv
while True:
    try:
        data = bytes.fromhex(input().strip())
    except Exception:
        print("Wrong input")
        exit(0)
    data = pad(data + flag)
    for i in range(0, len(data), 16):
        enc = hash_with_key(xor(enc, data[i:i+16]))
        print(enc.hex(), end='')
    print()
