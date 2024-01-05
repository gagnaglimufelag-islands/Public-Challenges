# Basic maths writeup

When we connect to the server, we can see that we have to solve 4 problems. 
We can use `pwntools` to parse the problems into python and solve them there.

```python3
from pwn import *

IP = "127.0.0.1" # server ip
PORT= 32000 # server port

conn = remote(IP, PORT)
conn.recvline()
```

## Problem 1
For the first problem, we see that we get 3 equations where we are suppose to find x. 
This is quite a well known problem in math, were if the modulo of the equations are pairwise coprime then there exists a solution for x.
We can use the chinese remainder theorem to find x, using sympy crt.

```python
from sympy.ntheory.modular import crt

conn.recvline()
conn.recvline()

mods = []
rems = []
for _ in range(3):
    line = conn.recvline().decode()
    print(line)
    r = int(line.split()[2])
    m = int(line.split()[4])
    rems.append(r)
    mods.append(m)

x,_ = crt(mods, rems)
conn.sendlineafter(b'> ', str(x).encode())

ans = conn.recvline().decode()
assert ans == 'correct!\n', f'{ans = }'
```
## Problem 2
For this problem we get to guess x 15 times and we will get back if the guess is below or above x. This is a classic binary search problem where we know the number is between 0 and 10000 and we guess `n=(0+10000)/2`.
Then we know if it is above or below and therefore we have cut our search space in half. Doing this over and over again leads us to x.

```python
conn.recvline()
conn.recvline()

lo, hi = 0, 10000
while True:
    m = (lo+hi)//2
    conn.sendline(str(m).encode())
    recv = conn.recvline().decode()[:-1]
    if recv.endswith('below x'):
        lo = m+1
    elif recv.endswith('above x'):
        hi = m-1
    else: 
        break

assert recv.endswith('correct!'), f'{recv = }'
```
## Problem 3
In this problem, we are suppose to supply a number n and we get back the lowest common multiplier (`lcm(n,x)`) of x and n and are then suppose to figure out x.
Since the lowest common multiplier of x and 1 is always x, we can just send 1 and get back x

```python
conn.recvline()
conn.recvline()

n = 1
conn.sendlineafter(b'> ',str(n).encode())
l = int(conn.recvline().split()[-1])

conn.sendlineafter(b'> ',str(l).encode())
recv = conn.recvline().decode()
assert recv == 'correct!\n', f'{recv = }'
```
## Problem 4
In this problem we are suppose to supply a number n and we get back the greatest common multiple (`gcd(n,x)`) of x and n and are then suppose to figure out x.
Since we know that x can be composed down into prime numbers and gcd gives us the multiple of the primes that are in common with n and x, if we supply all the primes under some number, a couple of times over, we can get back x.

We can use `sagemath` to get the multiple of primes


```python
from sage.all import Primes, prod
conn.recvline()
conn.recvline()

n = prod(Primes()[:10000])**3
conn.sendlineafter(b'> ',str(n).encode())
g = int(conn.recvline().split()[-1])

conn.sendlineafter(b'> ',str(g).encode())
recv = conn.recvline()
recv = conn.recvline().decode()
print(recv)
conn.close()
```

## Full solution

```python

from pwn import *

IP = "127.0.0.1" # server ip
PORT= 32000 # server port

conn = remote(IP, PORT)
conn.recvline()

## Problem 1 ##

from sympy.ntheory.modular import crt

conn.recvline()
conn.recvline()

mods = []
rems = []
for _ in range(3):
    line = conn.recvline().decode()
    print(line)
    r = int(line.split()[2])
    m = int(line.split()[4])
    rems.append(r)
    mods.append(m)

x,_ = crt(mods, rems)
conn.sendlineafter(b'> ', str(x).encode())

ans = conn.recvline().decode()
assert ans == 'correct!\n', f'{ans = }'

## Problem 2 ##

conn.recvline()
conn.recvline()

lo, hi = 0, 10000
while True:
    m = (lo+hi)//2
    conn.sendline(str(m).encode())
    recv = conn.recvline().decode()[:-1]
    if recv.endswith('below x'):
        lo = m+1
    elif recv.endswith('above x'):
        hi = m-1
    else: 
        break

assert recv.endswith('correct!'), f'{recv = }'

## Problem 3 ##

conn.recvline()
conn.recvline()

n = 1
conn.sendlineafter(b'> ',str(n).encode())
l = int(conn.recvline().split()[-1])

conn.sendlineafter(b'> ',str(l).encode())
recv = conn.recvline().decode()
assert recv == 'correct!\n', f'{recv = }'

## Problem 4 ##

from sage.all import Primes, prod
conn.recvline()
conn.recvline()

n = prod(Primes()[:10000])**3
conn.sendlineafter(b'> ',str(n).encode())
g = int(conn.recvline().split()[-1])

conn.sendlineafter(b'> ',str(g).encode())
recv = conn.recvline()
recv = conn.recvline().decode()
print(recv)
conn.close()
```
