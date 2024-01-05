import yaml
import logging
from sympy.ntheory.modular import crt
from sage.all import Primes, prod
from pwn import *
from pathlib import Path

logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


# For local binary testing
def solve(sh):
    sh.recvline()

    ### problem 1 (crt) ###
    sh.recvline()
    sh.recvline()
    mods = []
    rems = []
    for _ in range(3):
        line = sh.recvline().decode()
        r = int(line.split()[2])
        m = int(line.split()[4])
        rems.append(r)
        mods.append(m)

    x, _ = crt(mods, rems)
    sh.sendlineafter(b"> ", str(x).encode())

    ans = sh.recvline().decode()
    assert ans == "correct!\n", f"{ans = }"

    ### problem 2 (binary search) ###
    sh.recvline()
    sh.recvline()

    lo, hi = 0, 10000
    while True:
        m = (lo + hi) // 2
        sh.sendline(str(m).encode())
        recv = sh.recvline().decode()[:-1]
        if recv.endswith("below x"):
            lo = m + 1
        elif recv.endswith("above x"):
            hi = m - 1
        else:
            break

    assert recv.endswith("correct!"), f"{recv = }"

    ### problem 3 (lcm) ###
    sh.recvline()
    sh.recvline()

    n = 1
    sh.sendlineafter(b"> ", str(n).encode())
    l = int(sh.recvline().split()[-1])

    sh.sendlineafter(b"> ", str(l).encode())
    recv = sh.recvline().decode()
    assert recv == "correct!\n", f"{recv = }"

    ### problem 4 (gcd) ###
    sh.recvline()
    sh.recvline()

    n = prod(Primes()[:10000]) ** 3
    sh.sendlineafter(b"> ", str(n).encode())
    g = int(sh.recvline().split()[-1])

    sh.sendlineafter(b"> ", str(g).encode())
    recv = sh.recvline().decode()
    assert recv == "correct!\n", f"{recv = }"

    flag = sh.recvline().decode()
    assert FLAG in flag, flag


### IF BINARY ###
def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    test("localhost", 32000)
    # sh = process("./server.py")
    # solve(sh)
