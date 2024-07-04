import sys
from ctypes import CDLL, c_buffer

libc = CDLL("/lib/x86_64-linux-gnu/libc.so.6")

# Patent license 31337/2021: Tripple extra pie crust protection system
# All rights reserved by Unhackable Pie Storage System Inc.

buff1 = c_buffer(512)
buff2 = c_buffer(512)  # extra buffer just in case
buff3 = c_buffer(512)  # extra extra buffer just in case
buff4 = c_buffer(512)  # extra extra extra buffer just in case

print("Welcome to Unhackable Pie Storage System Inc. How may we help you?", flush=True)
print(">>> ", flush=True, end="")

# Only read in the first buffer, that is how we make sure the user does not input more than 512 bytes
libc.gets(buff1)

if b"python" != bytes(buff1[50:56]):
    print("but", flush=True)
    print(bytes(buff1), flush=True)
    print(bytes(buff1[50:56]), flush=True)
    sys.exit(1)

if b"is" != bytes(buff2[100:102]):
    print("c", flush=True)
    print(bytes(buff2), flush=True)
    print(bytes(buff2[100:102]), flush=True)
    sys.exit(2)

if b"memory" != bytes(buff3[13:19]):
    print("makes it", flush=True)
    print(bytes(buff3), flush=True)
    print(bytes(buff3[13:19]), flush=True)
    sys.exit(3)

if b"safe" != bytes(buff4[311:315]):
    print("great again", flush=True)
    print(bytes(buff4), flush=True)
    print(bytes(buff4[311:315]), flush=True)
    sys.exit(4)


with open(file="./flag.txt", mode="r", encoding="utf-8") as f:
    flag = f.read()

print("Holy strawberry pie, here is your flag:", flag, flush=True)
