import yaml
from base64 import b64decode
from pathlib import Path
import string

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'

def test():
    decoded = ""
    with open("src/chal.txt", "r") as f:
        data = f.read().rstrip()
        for key in range(len(alphabet)):
            dec = ""
            for e in data:
                dec += alphabet[(alphabet.find(e) - key) % len(alphabet)]
            dec += '=' * (4-(len(dec))%4)
            dec = b64decode(dec.encode())
            if all([dec[i] in list(string.printable.encode()) for i in range(len(dec))]):
                decoded = dec.decode()
    assert FLAG in decoded, decoded


if __name__ == "__main__":
    test()
