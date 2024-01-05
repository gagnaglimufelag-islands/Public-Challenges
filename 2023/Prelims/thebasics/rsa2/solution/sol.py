from pathlib import Path
import yaml

from itertools import product
from binascii import hexlify
from string import ascii_lowercase

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def decipher(c, e, n):
    for s in product(ascii_lowercase, repeat=4):
        flag = "gg{" + "".join(s) + "}"
        m = int("0x" + hexlify(flag.encode()).decode(), 16)
        if pow(m, e, n) == c:
            return flag


def test():
    wat = (HERE / "flag.txt").read_text()
    exec(wat)
    loc = locals()
    dec = decipher(loc["c"], loc["e"], loc["n"])
    assert dec == FLAG, dec
