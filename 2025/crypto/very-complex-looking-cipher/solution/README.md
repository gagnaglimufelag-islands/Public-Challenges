# Very complex looking cipher
Looking at the challenge file you can see a large equation that looks pretty intimdating. If you quickly look over it you might notice that all the numbers used only go up to 99.

Then instead of guessing what this equation does, we can just test it out with all the keys from 0 to 99 and see if we cannot get the flag out of it.

```python
import string
from src.chall import encrypt
enc = open('src/output.txt').read()

for key in range(100):
    map = {}
    for c in string.printable:
        e = encrypt(key, c)
        map[e] = c
    s = ''
    for e in enc:
        s += map[e]
    if s.startswith('gg{'): print(s)
```

Then this will print the flag.

`gg{caeser_cIpher_is_a_tradition_1_refuse_to_leAve_behind}`

Revealing that this was just a caeser cipher in disguise.
