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
