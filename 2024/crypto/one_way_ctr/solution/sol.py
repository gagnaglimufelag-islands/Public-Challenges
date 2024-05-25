import argparse
import yaml
import logging
from pwn import *
from pathlib import Path
import base64

logger = logging.getLogger("secretary")

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

def test(domain, port):
    solve(remote(domain, port))

def solve(io):
    def get(msg):
        io.sendline(base64.b64encode(msg))
        return (base64.b64decode(io.recvline()))

    a = (get(b'a'*16))
    b = (get(b'a'*17))

    flag = ""
    s = b[0]^a[0]^ord('a')
    flag += chr(s)
    i = 1
    while flag[-1] != '}':
        s = a[i]^b[i]^s
        flag += chr(s)
        i += 1

    assert FLAG in flag, flag



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", default="127.0.0.1", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    args = parser.parse_args()
    sh = process("./src/overwrite")
    solve(sh)
