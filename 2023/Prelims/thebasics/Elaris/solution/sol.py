import argparse
import yaml
import re
import subprocess
import logging
from pathlib import Path

logger = logging.getLogger("secretary")


# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


### IF STANDALONE (i.e. work on chall.txt) ###
def test(filename):
    out = subprocess.run(["zsteg", filename], capture_output=True).stdout.decode()
    flag = re.findall(r'gg\{.*\}', out)[0]
    logger.debug(flag)
    assert FLAG in flag, flag


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="File to run zsteg on")
    args = parser.parse_args()

    test(args.filename)
