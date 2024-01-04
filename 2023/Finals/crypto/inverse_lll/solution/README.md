# Inverse LLL writeup

We are given a file `server.py`

```python
#!/bin/python3
from sage.all import matrix, ZZ

with open('flag.txt','rb') as f:
    flag = list(f.read())
    
mat = [[0]*len(flag) for _ in range(len(flag))]
for i, c in enumerate(flag):
    mat[i][0] = c
    
print(f'Please provide {len(flag)-1}x{len(flag)} integers')
c = 0
for i in range(1,len(flag)):
    for j in range(len(flag)):
        mat[j][i] = int(input())

mat = matrix(ZZ, mat)
print('LLL:')
print(mat.LLL())
```

We can see that the flag is in the left column of the matrix and we control the rest of the values.

Since LLL is a lattice based reduction algorithm and it has no inverse, we need to find a clever way to extract the values of the flag.

One way to do this would be to put a large value (like 1000) for every dimension in the lattice except one, then when the LLL algorithm is run it will use that larger value as a basis vector for that dimension.
The matrix would then look something like this

```python
[[flag[0], 0,    0,    0,    ...],
 [flag[1], 1000, 0,    0,    ...],
 [flag[2], 0,    1000, 0,    ...],
 [flag[3], 0,    0,    1000, ...],
 ... ]
```
it would then have `flag[0]` in `0,0` position in the LLL output, doing this for every dimension would then give us the entire flag

So the solution would look like this
```python
from pwn import remote

IP = '0.0.0.0' # the ip of the server
PORT = 1234 # the port of the server

### Get the length of the flag
io = remote(IP, PORT)

r = io.recvline().decode()
flag_len = int(r.split('x')[-1].split()[0])
io.close()

def get_flag_char(nr):
    io = remote(IP, PORT)
    io.recvline().decode()
    # Add large values diagonally
    # shifted down depending on which character we are extracting
    for i in range(1,flag_len):
        for j in range(flag_len):
            if (j-nr)%flag_len == i:
                io.sendline(str(256).encode())
            else:    
                io.sendline(str(0).encode())
    io.recvline()
    val = int(io.recvline()[1:].split()[0])
    io.close()
    return val

flag = ''
for i in range(flag_len):
    flag += chr(get_flag_char(i))

print(flag)
```
