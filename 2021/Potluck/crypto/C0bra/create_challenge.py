#!/usr/bin/python3
flag = "10an{9R347357_C0Mm0n_D1v150R}"

# convert flag characters to ASCII code
flag_ascii = []
for i in flag:
    flag_ascii.append(str(ord(i)))
flag = ''.join(flag_ascii)
cipher_flag = int(flag) * 21
print("Cipher Flag:",cipher_flag)
