import requests
import argparse
import yaml
import logging
import requests
from pathlib import Path

logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test(url):
    session = requests.Session()
    flag = []
    while True:
        loc = session.get(url, allow_redirects=False).headers['location']
        if loc == '/success':
            break
        if len(loc) != 2:
            continue
        flag.append(loc[1])

    assert FLAG == (fl := ''.join(flag)), fl


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()
    test(args.url)
