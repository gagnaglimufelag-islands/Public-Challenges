# Keisara Dulkóðun writeup

If we translate the name of the challenge into english from Icelandic we can see that the name of the challenge is Ceaser encryption. 

Looking at the flag we can see some strange characters and since this is an Icelandic CTF we can summize that this is a ceaser cipher with a Icelandic alphabet.

Getting the alphabet from [wikipedia](https://en.wikipedia.org/wiki/Icelandic_orthography), we can decrypt it and get the flag

```python
alphabet = 'aábdðeéfghiíjklmnoóprstuúvxyýþæö'

data = ""
with open("chall.txt", "r") as f:
    data = f.read()

d = alphabet.index(data[0])
g = alphabet.index('g')
key = (d-g) % len(alphabet)
flag = ''
for c in data:
    if c in alphabet:
        flag += alphabet[(alphabet.index(c)-key) % len(alphabet)]
    else:
        flag += c

print(flag)
```