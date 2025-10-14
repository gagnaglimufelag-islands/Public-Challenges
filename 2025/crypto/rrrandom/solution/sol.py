import argparse
import yaml
import logging
import gmpy2
from pwn import *
from pathlib import Path
from Crypto.Util.number import *

logger = logging.getLogger("secretary")

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "challenge.yml"))["flags"][0]

# taken From: https://cryptohack.gitbook.io/cryptobook/untitled/recovering-the-modulus
def recover_n(pairings, e):
    pt1, ct1 = pairings[0]
    N = ct1 - pow(pt1, e)
    
    # loop through and find common divisors
    for pt,ct in pairings:
        val = gmpy2.mpz(ct - pow(pt, e))
        N = gmpy2.gcd(val, N)
    
    return N

def test(domain, port):
    while True:
        io = remote(domain, port)
        io.recvline()
        pairings = []
        for i in range(2):
            io.sendline(b'n')
            r = int(io.recvline().decode().split('r = ')[-1])
            enc = int(io.recvline())
            pairings.append((r,enc))

        n = str(recover_n(pairings, 3))

        encs = []
        for i in range(2):
            io.sendline(b'y')
            io.recvuntil(b'?')
            enc = int(io.recvline())
            encs.append(str(enc))
        io.close()
        out= (subprocess.run(["sage", "sol.sage"]+encs + [n], capture_output=True))
        try:
            flag = out.stdout.decode()
            flag = long_to_bytes(int(flag))
            break
        except Exception:
            continue

    assert FLAG in flag.decode(), FLAG.encode()+b' '+flag


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", default="127.0.0.1", nargs="?")
    parser.add_argument("port", default=32000, type=int, nargs="?")
    args = parser.parse_args()

    test(args.domain, args.port)
    
