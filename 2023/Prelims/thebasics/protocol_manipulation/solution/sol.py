import os
import argparse
import yaml
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test(url):
    res = os.popen(
        f"curl -s -X WAT '{url}/WAT?WAT=WAT' -d 'WAT=WAT' -H 'Cookie: WAT=WAT' -H 'WAT: WAT' -H 'User-Agent: WAT'"
    ).read()
    assert FLAG in res, res


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()

    test(args.url)
