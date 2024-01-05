from pwn import remote
from pathlib import Path
import logging
import argparse
import yaml

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

def solve(conn):
    conn.recvline()
    conn.sendlineafter(b'?: ', b'blue')

    conn.recvline()
    rec = conn.recvline()
    assert FLAG in rec.decode(), rec.decode()


def test(domain, port):
    sh = remote(domain, port)
    solve(sh)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", default="127.0.0.1", nargs="?")
    parser.add_argument("port", default=32000, type=int, nargs="?")
    args = parser.parse_args()
    conn = remote(args.domain, args.port)
    solve(conn)

