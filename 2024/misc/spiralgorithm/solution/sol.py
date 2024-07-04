from pwn import process, remote
import yaml
from pathlib import Path

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

def unspiral(text):
    correct = []
    lines = text.split()
    while lines:
        if len(lines) == 1:
            correct.append(lines[0])
            break
        first, *lines, pen = lines
        lines = list(map(''.join, zip(*lines)))
        if not lines:
            last = second = ''
        else:
            last, *lines, second = lines
            lines = list(map(''.join, zip(*lines)))
        correct.extend([first, second, pen[::-1], last[::-1]])

    return ''.join(correct)

def solve(p):
    p.recvuntil(b'----\n')

    for i in range(30):
        riddle = p.recvuntil(b'----').decode()
        p.recvline()
        p.sendline(unspiral('\n'.join(riddle.splitlines()[:-1])).encode())
        res = p.recvline()
        if b'Nope' in res:
            print(riddle)
            print(unspiral('\n'.join(riddle.splitlines()[:-1])).encode())
            print(p.recvline())
        p.recvuntil(b'----\n')


    flag = p.recvuntil(b'----').decode()
    return unspiral('\n'.join(flag.splitlines()[:-1]))

def test(domain, port):
    p = remote(domain, port)
    res = solve(p)
    assert FLAG in res, res

if __name__ == '__main__':
    p = process(['python', 'server.py'])
    print(solve(p))


