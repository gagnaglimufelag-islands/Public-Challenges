import yaml
from pathlib import Path
import logging

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


logger = logging.getLogger("secretary")


def test():
	data = open(HERE / 'files/chall.png','rb').read()

	b = ''
	for d in data.split(b'IDAT')[1:]:
		if len(d)-4*2 == 10:
			b += '1'
		else:
			b += '0'
	l = 100
	flag = (int(b[:l*8],2).to_bytes(l,'big').split(b'}')[0].decode() + '}')
	assert FLAG in flag, f'{flag}'

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)

	test()

