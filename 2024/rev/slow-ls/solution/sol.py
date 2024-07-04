import re
import yaml
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test():
    with open(HERE / "src" / "main.c", "r") as f:
        match = re.search(r"int sums\[\d+\]\s=\s\{([\d,\s]+)\}", f.read())
        assert match is not None

        nums = [int(x) for x in match.group(1).split(", ")]
        out = ""

        for i, j in enumerate(nums):
            if i % 3 == 0:
                tmp = j - 23
                out += chr(int(tmp))
            elif i % 3 == 1:
                tmp = j * 2 - 42
                tmp = (j + 42) / 2
                out += chr(int(tmp))
            elif i % 3 == 2:
                tmp = ((j + 50) * 2 - 256) / 2
                out += chr(int(tmp))

        assert FLAG in out, out

if __name__ == "__main__":
    test()
