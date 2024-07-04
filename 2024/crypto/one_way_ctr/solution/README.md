# One way CRT

The trick to solving this problem is to notice that we can send 16 and 17 base64 encoded characters, then we can just use xor to extract the flag characters one by one.

### Solve script

```python
from pwn import *
import base64

io = remote('localhost', 6666)
def get(msg):
    io.sendline(base64.b64encode(msg))
    return (base64.b64decode(io.recvline()))

a = (get(b'a'*16))
b = (get(b'a'*17))

flag = ""
s = b[0]^a[0]^ord('a')
flag += chr(s)
i = 1
while flag[-1] != '}':
    s = a[i]^b[i]^s
    flag += chr(s)
    i += 1

print(flag)
```
