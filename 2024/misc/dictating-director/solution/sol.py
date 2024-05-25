import subprocess
import argparse
import yaml
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test(url):
    result = subprocess.run(
        ["curl", "-L", "--max-redirs", "10000", url], capture_output=True, text=True
    )
    assert FLAG in result.stdout, result.stdout


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()

    test(args.url)
