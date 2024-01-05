import argparse
import yaml
import logging
from pwn import *
from pathlib import Path

logger = logging.getLogger("secretary")


# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


# For local binary testing
def solve(sh):
    try:
        import itertools
    except ImportError:
        print("Error Importing 'itertools'")
        exit(0)
    def level_two():
        def xor_num(num):
            xor_num_array = [55, 245, 138, 125, 258, 33]
            for i in range(len(xor_num_array)):
                num = num ^ xor_num_array[i]
            return num
        i = 0
        while True:
            if xor_num(i) == 505:
                level_two = str(i)
                break
            i += 1
        return level_two

    def level_three():
        numbers = '0123456789'
        s = ''
        for i in itertools.product(numbers, repeat=4):
            try:
                passcode = s + ''.join(i)
                sh.sendline(passcode.encode())
                data = sh.recv()
                if b"gg{" in data:
                    flag = data.decode().split()[-1]
                    print()
                    log.success(flag)
                    return flag
            except EOFError:
                log.warning("Reached EOF!")
                log.info("Tru re-running")
                break
    sh.sendline(str(int(0xdeadbeef)).encode())
    sh.sendline(str(level_two()).encode())
    flag = level_three()
    assert FLAG in flag, flag


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
        sh = process("./w1zArD")
        solve(sh)
