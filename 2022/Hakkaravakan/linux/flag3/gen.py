from pathlib import Path
from string import ascii_lowercase, printable
from random import randint, choice
from shutil import rmtree
from datetime import datetime
from itertools import repeat
import os
from pathlib import Path

OUT = Path('out')

ROOT_DIRS = ['var,' 'usr', 'etc', 'bin']

BLACKLIST = [
    'apt.conf.d',
    'python3.8',
    'dpkg.cfg.d',
    'default.target.wants',
]

DIRS = []

for d in ROOT_DIRS:
    DIRS.extend([x for x in (Path('/') / d).glob('**/*') if x.is_dir() and not any(y in str(x) for y in BLACKLIST)])

for f in OUT.glob('*'):
    f.unlink()

def randdate():
    while True:
        try:
            d = datetime(randint(1975, 2022), randint(1,2), randint(1, 31), randint(0, 23), randint(0, 59), randint(0, 59))
            return d
        except:
            # invalid date
            pass

def randstr():
    return ''.join(choice(ascii_lowercase) for _ in range(randint(3,7)))

# def randdir():
#     l = randint(1, 10)
#     d = '/'.join(choice(ascii_lowercase) for _ in range(l))
#     path = OUT / d
#     path.mkdir(exist_ok=True, parents=True)
#     return path

def randdir():
    return choice(DIRS)

def addfile(content, date=None):
    file = OUT / randstr()
    file.write_text(content)
    date = date or randdate()
    os.utime(file, (date.timestamp(), date.timestamp()))
    return file.name

flag = Path('flag3.txt').read_text().strip()

dates = [randdate() for _ in flag]

file = OUT / 'run.sh'

with file.open('w') as f:
    for d, c in zip(sorted(dates), flag):
        rname = addfile(c, date=d)
        rdir = randdir()
        print(f'mv "{rname}" "{rdir}"', file=f)
        print(f'chown ghost:ghost "{rdir / rname}"', file=f)

