import string
import random
from pathlib import Path
import yaml
import subprocess

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

def gen():
    alpha = string.printable

    cond = []
    for c in alpha:
        for k in range(100):
            cond += [f"(({alpha.find(c)}==c and k=={k})*{(alpha.find(c)+k) % len(alpha)})"]
    random.shuffle(cond)


    prefix = '''import string

a = string.printable
def encrypt(k, message):
    message = [a.find(c) for c in message]
    return (''.join([a[sum(['''
    suffix = f'''])] for c in message]))

flag = '{FLAG}'
if __name__ == '__main__':
    key = 34
    print(encrypt(key, flag))
    '''
    open('src/donotshare.py','w').write(prefix+",".join(cond)+suffix)
    
    with open('src/output.txt', "w") as outfile:
        subprocess.run(['python3','src/donotshare.py'], stdout=outfile)
    


if __name__ == "__main__":
    gen()
