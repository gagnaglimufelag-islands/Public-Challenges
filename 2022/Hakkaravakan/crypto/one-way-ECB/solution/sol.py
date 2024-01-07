from pathlib import Path
from pwn import *
import argparse
import string
import yaml

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def solve(conn):
    def recv(msg):
        conn.recvuntil(b": ")
        conn.sendline(msg.hex().encode())
        return bytes.fromhex(conn.recvline()[:-1].decode())

    flag = b""
    for blk in range(3):
        for i in range(16):
            prefix = b"\0" * (15 - i)
            real = recv(prefix)
            for c in string.printable.encode():
                test = recv(prefix + flag + bytes([c]))
                if (
                    test[16 * (blk) : 16 * (blk + 1)]
                    == real[16 * (blk) : 16 * (blk + 1)]
                ):
                    flag += bytes([c])
                    # print(f'{flag = }')
                    break
    assert FLAG in flag.decode(), flag.decode()


def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", default="127.0.0.1", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    args = parser.parse_args()
    conn = remote(args.domain, args.port)
    solve(conn)
