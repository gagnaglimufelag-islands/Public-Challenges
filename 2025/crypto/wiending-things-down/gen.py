from Crypto.Util.number import *
import random

import yaml
from base64 import b64encode
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

flag = FLAG.encode()

p = getPrime(1024)
q = getPrime(1024)
n = p*q
d = getPrime(16)

phi = (p-1)*(q-1)
e = pow(d,-1,phi)

l = 1024*2 - len(flag)*8 
padded = bytes_to_long(flag)*pow(2,l) + random.getrandbits(l)

out = (f'{n = }\n')
out += (f'{e = }\n')
out += ('enc = '+ str(pow(padded, e, n)))

open('src/output.txt','w').write(out)
