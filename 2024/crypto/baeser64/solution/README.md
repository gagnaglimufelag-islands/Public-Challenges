# Baeser64

Looking at the name of the problem, one can summize that it has something to do with base64 and caeser cipher.

Below is a script that decrypts the ceaser cipher and base64 decodes the string to get the flag

```python
import string
from base64 import b64decode

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
enc = "PUT FLAG HERE"
for key in range(len(alphabet)):
    dec = ""
    for e in enc:
        dec += alphabet[(alphabet.find(e) - key) % len(alphabet)]
    dec += '=' * (4-(len(dec))%4)
    dec = b64decode(dec.encode())
    if all([dec[i] in list(string.printable.encode()) for i in range(len(dec))]):
        print(dec.decode())
```

