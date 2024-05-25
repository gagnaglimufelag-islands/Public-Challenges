#!/usr/bin/env python3
from hashlib import sha256
import base64
import os

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

def encrypt(msg, key):
    iv = int.from_bytes(msg[:16], 'big')
    msg = msg[16:]
    enc = b''
    for i in range(len(msg)//16+1):
        blk = msg[i*16:(i+1)*16]
        blk += os.urandom(16-(len(blk) % 16))
        enc += xor(blk, sha256(key + iv.to_bytes(16, 'big')).digest()[:16])
        iv += 1
    return enc

flag = b"gg{this_is_fake_flag}"
key = os.urandom(16)
while True:
    try:
        iv = input()
        if len(iv) != 24: 
            print("IV needs to be 16 bytes long")
            continue
    except Exception:
        continue
    msg = base64.b64decode(iv) + flag

    print(base64.b64encode(encrypt(msg, key)).decode())

