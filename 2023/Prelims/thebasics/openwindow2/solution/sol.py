import yaml
import logging
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

logger = logging.getLogger("secretary")


def test():
    prob = (HERE / "openwindow2.py").read_text()
    rule = re.compile(r"correct_bytes = (\[[^\]]*\])", re.MULTILINE)
    m = rule.search(prob)
    assert m
    key = 3 * "x" + "".join(map(chr, eval(m.group(1)))) + "x"

    res = subprocess.run(
        ["python", str(HERE / "openwindow2.py")],
        input=key,
        universal_newlines=True,
        capture_output=True,
    )
    assert FLAG in (o := res.stdout), o


if __name__ == "__main__":
    test()
