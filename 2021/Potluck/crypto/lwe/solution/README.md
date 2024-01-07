# Solution for Proper LWE Implementation
The main vulnerability here is that the ```p3``` is being used as the publicly available random data and ```p2``` is being used as the secret error (the key). ```p3``` is the product of a large prime (```p1```) and a 40-bit prime (```p2```), this number can be factories quickly with Pollard's Rho algorithm and the error can be removed from the ciphertext. Then to solve for the secret data we can use the least square method ```python
from numpy.linalg import lstsq
secret = lstsq(random, ciphertext)[0]
secret = map(lambda x: chr(int(round(x[0]))), secret[0])
print '10an{' + ''.join(secret) + '}'
```
this wil print the flag
