import yaml
import subprocess
import logging
from pwn import *
from pathlib import Path

logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test():
    context.terminal = ['kitty', 'sh', '-c']
    p = process(str(HERE / "chal/dbg"))
    gdb.attach(p, gdbscript=f'''
    set logging file {HERE / 'flag.txt'}
    set logging off
    b *main+920
    r
    set logging on
    x/s $eax
    set logging off
    detach
    quit
    ''')
    ffile = HERE / 'flag.txt'
    flag = ffile.read_text().strip()
    ffile.unlink()
    flag = flag.replace('"', '')
    log.success(flag)
    assert FLAG in flag, flag


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    test()
