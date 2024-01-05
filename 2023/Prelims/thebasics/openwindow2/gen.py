import re
import yaml
import random
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

correct_bytes = []
for c in FLAG[3:-1]:
    correct_bytes.append(ord(c))

rand_byte = random.choice(correct_bytes)
rand_byte_index = correct_bytes.index(rand_byte)
rand_shift = random.choice(range(1, 10))

correct_bytes[rand_byte_index] = f"{rand_byte << rand_shift} >> {rand_shift}"

new_correct_bytes = str(correct_bytes).replace("'", "")
old_chall = (HERE / "openwindow2.py").read_text()
rule = re.compile(r"correct_bytes = \[[^\]]*\]", re.MULTILINE)
old_correct_bytes = rule.search(old_chall)
new_chall = old_chall.replace(
    old_correct_bytes.group(0), f"correct_bytes = {new_correct_bytes}"
)

with open("openwindow2.py", "w") as f:
    f.write(new_chall)
