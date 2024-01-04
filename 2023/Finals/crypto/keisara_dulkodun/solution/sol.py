from pathlib import Path
import logging
import yaml

from gen import alphabet

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]



def test():
	data = ""
	with open("chall.txt", "r") as f:
		data = f.read()
	d = alphabet.index(data[0])
	g = alphabet.index('g')
	key = (d-g) % len(alphabet)
	ans = ''
	for c in data:
		if c in alphabet:
			ans += alphabet[(alphabet.index(c)-key) % len(alphabet)]
		else:
			ans += c

	assert FLAG in ans, ans


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    
    test()
