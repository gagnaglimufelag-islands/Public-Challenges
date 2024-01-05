import os
import yaml
import logging
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

logger = logging.getLogger("secretary")


def test():
    first = os.popen(f"strings {HERE / 'animal_generator'} | grep -E 'gg{{'").read().strip("\n")
    second = os.popen(f"strings {HERE / 'animal_generator'} | grep -E '^ '").read().strip("\n")
    third = os.popen(f"strings {HERE / 'animal_generator'} | grep -E '}}'").read().strip("\n")
    flag = f"{first}{second}{third}"
    assert FLAG in flag, flag


if __name__ == "__main__":
    test()
