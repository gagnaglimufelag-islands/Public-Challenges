import yaml
import random
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

key = random.randint(1, 255)
print(key)

encrypted = bytes([b ^ key for b in FLAG.encode()])
print(encrypted)

with open("enc.txt", "wb") as f:
    f.write(encrypted)
