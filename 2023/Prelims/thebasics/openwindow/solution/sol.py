import yaml
import logging
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

logger = logging.getLogger("secretary")


def test():
    prob = (HERE / "openwindow.py").read_text()
    m = re.search('== "([^ ]+)"', prob)
    assert m
    passw = 3 * "x" + "".join(m.group(1)[::-1]) + "x"

    res = subprocess.run(
        ["python", str(HERE / "openwindow.py")],
        input=passw,
        universal_newlines=True,
        capture_output=True,
    )
    assert FLAG in (o := res.stdout), o


if __name__ == "__main__":
    test()
