# One way ECB writeup

If you read `files/chall.py` you can see that the server takes in a prefix and appends the flag to it and then pads those bytes.

```python
data = prefix + flag
data = pad(data)
```
the padding is just a normal deterministic padding so we don't need to think about it too much.

Then it takes every 16 bytes of `data` and hashes those bytes, giving us the output for each hashed block.

```python
for i in range(0,len(data), 16):
    enc += hash_with_key(data[i:i+16])
print(enc)
```

This is all in a while loop so we can give it different prefixes and try and see if we cannot extract the flag.

Looking at the `hash_with_key` function
```python
key = urandom(16)

def hash_with_key(msg: bytes):
    return sha256(msg + key).digest()[:16]
```

we can see that the key never changes during our connection to the server, therefore if we send 15 bytes of data, we will have a hashed 15 bytes plus the first byte in our flag.
If we knew the key, then we would be able to try all the possible characters locally to find the first character in our flag.
```python
for c in string.printable():
    if hsh == hash_with_key(b'a'*15 + c.encode()): 
        print(f'{c = }')
```
where `hsh` is the first 16 bytes output from the server with input `b'a'*15`.

However since we don't know the key, we must ask the server instead to give us the hashed output for all the possible characters.

we first create a function so we can easily get the answer from the server using `pwntools`

```python
from pwn import *
conn = remote(IP,PORT)

def recv(msg):
    conn.recvuntil(b': ')
    conn.sendline(msg.hex().encode())
    return bytes.fromhex(conn.recvline()[:-1].decode())
```

Then for every character we ask it what the hash is for all those bytes

```python
prefix = b'a'*15
hsh = recv(prefix)[:16]
for c in string.printable:
    test = recv(prefix + c.encode())[:16]
    if test == hsh:
        print(f'{c = }')    
```
Then assuming we did everything correctly, we should print out the first character of the flag.

We can repeat this for all the characters in the same 16 byte block, just by removing one `b'a'` from our prefix for every flag character we get and adding the known flag character when we test it

```python
flag = b''
for i in range(16):
    prefix = b'a'*(15-i)
    hsh = recv(prefix)[:16]
    for c in string.printable:
        test = recv(prefix + flag + c.encode())[:16]
        if test == hsh:
            flag += c.encode()
            print(f'{flag = }')
            break
```

Then since the flag is longer then 16 bytes, we just do the same thing for the other blocks

```python
flag = b''
for blk in range(3):
    for i in (range(16)):
        prefix = b'\0'*(15-i)
        hsh = recv(prefix)
        for c in string.printable:
            test = recv(prefix + flag + c.encode())
            if test[16*blk:][:16] == hsh[16*blk:][:16]:
                flag += c.encode()
                print(f'{flag = }')
                break
```

The full solution script is then

```python
from pwn import *

IP = "127.0.0.1" # server ip
PORT= 32000 # server port

conn = remote(IP,PORT)

def recv(msg):
    conn.recvuntil(b': ')
    conn.sendline(msg.hex().encode())
    return bytes.fromhex(conn.recvline()[:-1].decode())

flag = b''
for blk in range(3):
    for i in (range(16)):
        prefix = b'\0'*(15-i)
        hsh = recv(prefix)
        for c in string.printable:
            test = recv(prefix + flag + c.encode())
            if test[16*blk:][:16] == hsh[16*blk:][:16]:
                flag += c.encode()
                print(f'{flag = }')
                break
```





