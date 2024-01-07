from pathlib import Path
from string import ascii_lowercase, printable
from random import randint, choice
from shutil import rmtree
from datetime import datetime
import os

OUT = Path('ransom')

if OUT.exists():
    rmtree(OUT)
OUT.mkdir()

def randdate():
    while True:
        try:
            d = datetime(2022, randint(1,2), randint(1, 31), randint(0, 23), randint(0, 59), randint(0, 59))
            if d.month == 2 and d.day == 22:
                continue
            return d
        except:
            # invalid date
            pass

def randdir():
    l = randint(1, 10)
    d = '/'.join(choice(ascii_lowercase) for _ in range(l))
    path = OUT / d
    path.mkdir(exist_ok=True, parents=True)
    return path

def addfile(path, part=None, content=None, date=None):
    if content is None:
        content = choice(printable)
    if part is None:
        part = randint(0,100)
    file = path / f'p{part}'
    file.write_text(content)
    date = date or randdate()
    os.utime(file, (date.timestamp(), date.timestamp()))

for _ in range(1000):
    r = randdir()
    addfile(r)


flag = Path('../flag3.txt').read_text().strip()

for i, c in enumerate(flag):
    r = randdir()
    date = datetime(2022, 2, 22, randint(0, 23), randint(0, 59), randint(0, 59))
    addfile(r, part=i, content=c, date=date)



