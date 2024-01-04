import yaml
from pathlib import Path 
import subprocess

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


with open("flag.txt", "w") as f:
    f.write(FLAG)

with open('files/out.txt','w') as f:
    r = subprocess.run(['python3', 'files/chall.py'], stdout=f)


