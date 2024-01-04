# Indeed Dinner After Tomorrow

If you look at the size of the `IDAT` chunks using for example
```
pngcheck -c -v -t chall.png | less
```

you can see that the first is length 13 for the `IHDR` chunk and then there is a sequance of size 10 and 20. 
If you then extract that sequence and make size 10 be `1` and size 20 be `0` and then convert those to bytes, the flag is in the first couple of bytes.

```python
data = open('files/chall.png','rb').read()

b = ''
for d in data.split(b'IDAT')[1:]:
	if len(d)-4*2 == 10:
		b += '1'
	else:
		b += '0'

l = 100
flag = (int(b[:l*8],2).to_bytes(l,'big').split(b'}')[0].decode() + '}')
print(flag)
```

