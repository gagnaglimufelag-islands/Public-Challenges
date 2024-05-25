import yaml
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

nums = []

for i, j in enumerate(FLAG):
    if i % 3 == 0:
        tmp = ord(j) + 23
        nums.append(tmp)
    elif i % 3 == 1:
        tmp = ord(j) * 2 - 42
        nums.append(tmp)
    elif i % 3 == 2:
        tmp = (ord(j) * 2 + 256) / 2 - 50
        nums.append(int(tmp))

print(f"int sum[{len(FLAG)}] = {{{', '.join(str(x) for x in nums)}}};")
