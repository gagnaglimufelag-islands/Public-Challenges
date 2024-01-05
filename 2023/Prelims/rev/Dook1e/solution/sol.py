import yaml
import argparse
import logging
from pwn import *
from pathlib import Path


logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


# For local binary testing
def solve(sh):
    try:
        from ctypes import CDLL
    except ImportError:
        log.Error("Failed To Import CDLL from Ctypes!")
    libc = CDLL(HERE / "chal/libc.so.6") # Path to LIBC
    libc.srand(678485)
    correct_nums = [str(libc.rand() % 1000 + 1) for x in range(5)]
    logger.debug(f"Correct NUMS: {correct_nums}")
    for num in correct_nums:
        sh.sendline(num.encode())
    flag = sh.recvall().split()[-1].decode()
    logger.debug(flag)
    sh.close()
    assert FLAG in flag, flag


def test(domain, port):
    sh = remote(domain, port)
    solve(sh)



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument("domain", default="127.0.0.1", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    args_argparse = parser.parse_args()

    if args.REMOTE:
        test(args_argparse.domain, args_argparse.port)
    else:
        sh = process("chal/Dook1e")
        solve(sh)
