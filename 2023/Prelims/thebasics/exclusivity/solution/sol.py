from pathlib import Path
import yaml

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def break_xor(ciphertext):
    for key in range(256):
        plaintext = bytearray([c ^ key for c in ciphertext])
        try:
            message = plaintext.decode()
            if message.startswith(FLAG[: FLAG.find("{") + 1]):
                return message
        except UnicodeError:
            pass
    return "flag not found"


def test():
    with open(HERE / "enc.txt", "rb") as f:
        ciphertext = f.read()

    dec = break_xor(ciphertext)
    assert dec == FLAG, dec


if __name__ == "__main__":
    test()
