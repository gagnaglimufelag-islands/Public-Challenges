import yaml
from base64 import b64encode, b64decode

MESSAGE = yaml.safe_load(open('meta.yml'))['flags']

def encrypt(s):
    return b64encode(s).decode()[::-1]

def main():
    with open('kringle-crush.txt', 'w') as f:
        print(encrypt(MESSAGE.encode()), file=f)

main()

def decipher(t):
    return b64decode(t[::-1]).decode()


def solve():
    t = open('andor.txt').read()

    print(decipher(t))

