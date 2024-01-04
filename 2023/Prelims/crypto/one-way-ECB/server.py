#!/bin/python3
from hashlib import sha256
from os import urandom

key = urandom(16)

def hash_with_key(msg: bytes):
    return sha256(msg + key).digest()[:16]
def pad(msg: bytes):
    if len(msg) % 16 == 0: padding_len = 16
    else: padding_len = -len(msg)%16
    return msg + bytes([padding_len])*padding_len

with open("flag.txt",'rb') as f:
    flag = f.read().strip()

while True:
    print("prefix (hex): ", end="")
    try:
        prefix = bytes.fromhex(input().strip())
    except Exception:
        print("wrong input")
        exit(0)
    data = prefix + flag
    data = pad(data)
    enc = b''
    for i in range(0,len(data), 16):
        enc += hash_with_key(data[i:i+16])
    print(enc.hex())

