# Open Window
An introductory rev challenge for people with no CTF experience. The challenge
is a simple python script that switches each character in the first halve with
a respective character in the second half. In simpler terms, the python script
is reversing the given string.

So to solve the challenge, take the string in the binary, reverse it and 
surround with `gg{PASSW}` and you will be given the flag:

```bash
python openwindow.py 
Enter password: gg{th30lsw1tch4r0o0}
gg{th30lsw1tch4r0o0}
```
