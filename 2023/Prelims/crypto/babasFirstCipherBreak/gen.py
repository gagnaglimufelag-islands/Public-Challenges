from subprocess import run
from base64 import b64encode
from pathlib import Path 
import yaml # soyml

cwd = Path(__file__).parent
FLAG = yaml.safe_load(open(cwd / "meta.yml"))["flags"]

with open('flag.txt', 'w') as f:
	f.write(FLAG)

run(['python3', 'encrypt.py', 'flag.txt'])
run(['python3', 'encrypt.py', 'whatYouEgg?HeStabsHim.png'])
