import yaml
from random import randint, random, shuffle, sample
from pathlib import Path
from shutil import rmtree
from string import Template
from zipfile import ZipFile
import subprocess

here = Path(__file__).parent

meta = yaml.safe_load(open(here / 'meta.yml'))
flag = meta['flags'].encode()

encrypted = list(flag)

N = len(flag)

TEMPLATE = Template('''def ${name}(flag):
    ${code}
''')

FUNCTION_NAMES = ['wat', 'why', 'how', 'when', 'who', 'rotate', 'enc', 'encr', 'renc']

out = here / 'repo'
rmtree(out, ignore_errors=True)
out.mkdir()
subprocess.run('git init', shell=True, cwd=out)
subprocess.run('git config user.name "Bill Lumbergh"', shell=True, cwd=out)
subprocess.run('git config user.email "b.lumbergh@initech.com"', shell=True, cwd=out)

DESTROYED = {}

for f in FUNCTION_NAMES:
    file = (out / f).with_suffix('.py')
    body = []
    bady = []
    for _ in range(randint(300, 500)):
        ind = randint(0, N-1)
        k = randint(0, 255)
        encrypted[ind] ^= k
        body.append(f'flag[{ind}] ^= {k}')

        if random() < 0.01:
            bady.append(f'flag[{ind}] ^= {randint(0, 255)}')
        else:
            bady.append(f'flag[{ind}] ^= {k}')
    file.write_text(TEMPLATE.substitute(name=f, code='\n    '.join(body)))
    DESTROYED[f] = TEMPLATE.substitute(name=f, code='\n    '.join(bady))


main = out / 'main.py'
imports = '\n'.join(f'from {n} import {n}' for n in FUNCTION_NAMES)
calls = '\n'.join(f'{n}(flag)' for n in FUNCTION_NAMES)

main_code = f'''{imports}

flag = {encrypted}

{calls}

print(bytes(flag))
'''
main.write_text(main_code)

subprocess.run('git add *.py', shell=True, cwd=out)
subprocess.run('git commit -m "Sensitive stuff"', shell=True, cwd=out)

for f in FUNCTION_NAMES:
    file = (out / f).with_suffix('.py')
    file.write_text(DESTROYED[f])

(here / 'fit1.zip').unlink(missing_ok=True)
with ZipFile(here / 'fit1.zip', 'w') as zf:
    for f in (here / 'repo').glob('**/*'):
        if f.is_file():
            zf.write(f, f.relative_to(here))

        # subprocess.run(f'cd {here} && zip -r fit1 {out}', shell=True)

# Cleanup
# rmtree(out)
