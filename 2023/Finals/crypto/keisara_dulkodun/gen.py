import yaml
from pathlib import Path 
from base64 import b64encode

alphabet = 'aábdðeéfghiíjklmnoóprstuúvxyýþæö'

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

key = 10
enc = ''
for c in FLAG:
	if c in alphabet:
		enc += alphabet[(alphabet.index(c)+key) % len(alphabet)]
	else:
		enc += c

with open("chall.txt", "w") as f:
    f.write(enc)
