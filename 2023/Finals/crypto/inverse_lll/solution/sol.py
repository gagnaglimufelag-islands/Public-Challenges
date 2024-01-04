from pathlib import Path
from pwn import *
import logging
import argparse
import yaml

logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test(domain, port):
    io = remote(domain, port)

    r = io.recvline().decode()
    flag_len = int(r.split('x')[-1].split()[0])
    io.close()

    def get_flag_char(nr):
        io = remote(domain, port)
        io.recvline().decode()
        for i in range(1,flag_len):
            for j in range(flag_len):
                if (j-nr)%flag_len == i:
                    io.sendline(str(256).encode())
                else:    
                    io.sendline(str(0).encode())
        io.recvline()
        val = int(io.recvline()[1:].split()[0])
        io.close()
        return val
    s = ''
    for i in range(flag_len):
        s += chr(get_flag_char(i))
    
    assert FLAG in s, s 



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()

    parser.add_argument("domain", default="127.0.0.1", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    args = parser.parse_args()

    test(args.domain, args.port)
