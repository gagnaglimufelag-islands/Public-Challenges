from pathlib import Path
import yaml
from binascii import unhexlify

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def decipher(c, d, n):
    m = pow(c, d, n)
    return unhexlify(hex(m)[2:]).decode()


def test():
    wat = (HERE / "flag.txt").read_text()
    exec(wat)
    loc = locals()
    dec = decipher(loc["c"], loc["d"], loc["n"])
    print(dec)
    assert dec == FLAG, dec


if __name__ == "__main__":
    test()
