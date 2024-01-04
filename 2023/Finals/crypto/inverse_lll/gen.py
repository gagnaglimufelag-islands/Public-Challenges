import yaml
from pathlib import Path 
from base64 import b64encode

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

with open("flag.txt", "w") as f:
    f.write(FLAG)
