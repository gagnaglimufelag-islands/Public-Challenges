from pathlib import Path
import logging
import yaml
import re
import argparse

from pwn import *
import string

logger = logging.getLogger("secretary")

# For OOB interaction, if required
OAST = re.compile(r"\[.*INF.*\] ([a-z0-9]+\.[a-z0-9]+\.[a-z]+)")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]



def solve(io):
    def recv(msg):
        io.sendline(msg.hex().encode())
        return bytes.fromhex(io.recvline().decode())

    last_hsh = recv(b'')[-16:]
    flag = b''
    for blk in range(1,4):
        for i in (range(16)):
            prefix = b'\0'*(15-i)
            hsh = recv(last_hsh + prefix)
            last_hsh = hsh[-16:]
            for c in string.printable:
                test = recv(last_hsh + prefix + flag + c.encode())
                last_hsh = test[-16:]
                if test[16*blk:][:16] == hsh[16*blk:][:16]:
                    flag += c.encode()
                    #print(f'{flag = }')
                    break
    flag = flag.decode() 
    print(flag)
    assert FLAG in flag, flag

def test(domain, port):
    sh = remote(domain, port)
    solve(sh)
            
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    
    parser.add_argument("domain", default="127.0.0.1", nargs="?")
    parser.add_argument("port", default=1337, type=int, nargs="?")
    args = parser.parse_args()
    test(args.domain, args.port)
