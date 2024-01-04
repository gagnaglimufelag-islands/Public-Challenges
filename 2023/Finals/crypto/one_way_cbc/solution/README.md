# One way CBC Writeup

This is a lot like the challenge [One Way ECB](https://github.com/gagnaglimufelag-islands/writeups/tree/master/2023/Prelims/crypto/One%20Way%20ECB) that was in the gagnaglíman preliminaries, 
the only difference is that now we have an IV and the last hashed blocked is xored with the current block.

Since we always know the previous blocks hash, we can modify the solution script from One way ECB and just add the previous blocks hash as input and then the first block will always be 16 zero bytes.

Then the solution script will look like something this
```python
from pwn import *

IP = '0.0.0.0' # The remote ip
PORT = 1337 # the remote port

io = remote(IP, PORT)

def recv(msg):
    io.sendline(msg.hex().encode())
    return bytes.fromhex(io.recvline().decode())

last_hsh = recv(b'')[-16:]
flag = b''
for blk in range(1,4):
    for i in (range(16)):
        prefix = b'\0'*(15-i)
        hsh = recv(last_hsh + prefix)
        last_hsh = hsh[-16:]
        for c in string.printable:
            test = recv(last_hsh + prefix + flag + c.encode())
            last_hsh = test[-16:]
            if test[16*blk:][:16] == hsh[16*blk:][:16]:
                flag += c.encode()
                print(f'{flag = }')
                break
```

Giving us the flag `gg{1_gu3ss_I_g0t_tO_g1ve_UP!!!}`
