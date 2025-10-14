import yaml
from pathlib import Path
import string
from src.chall import encrypt

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

def test():
    enc = open('src/output.txt').read()

    flagin = ''
    for key in range(100):
        map = {}
        for c in string.printable:
            e = encrypt(key, c)
            map[e] = c
        s = ''
        for e in enc:
            s += map[e]
        flagin += s

    assert FLAG in flagin, flagin 

if __name__ == "__main__":
    test()
