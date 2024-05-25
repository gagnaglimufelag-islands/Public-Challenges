import yaml
from base64 import b64encode
from pathlib import Path
import string
import random

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
key = 42

def gen():
    encoded = b64encode(FLAG.encode()).decode().rstrip('=')

    enc = b""
    for e in encoded:
        enc += alphabet[(alphabet.find(e) + key) % len(alphabet)].encode()

    with open("src/chal.txt", "w") as f:
        f.write(enc.decode())


if __name__ == "__main__":
    gen()
