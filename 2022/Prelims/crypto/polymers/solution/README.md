# Polymer
This challenge is pretty trivial, all thats happening is that each letter of your password is a coefficient in a polynomial $P(x)$. That polynomial and the secret polynomial $S(x)$ are then evaluated at `ID` and subtracted. $S(ID) - P(ID)$. If the result is non-zero the result is returned to the user

Recovering the secret polynomial can be done by setting `ID` to any value greater or equal than 128 because all of the coefficients are ascii values and therefore smaller than 128 and sending whatever you want as the password. Then you can recover $S(ID)$ by adding $P(ID)$ to the digest. Then every coefficient can be recovered by taking $S(ID) \pmod{ID}$ and then $S(ID) = S(ID) // ID$

Instead of recovering each coefficient one by one you could just set `ID` equal to 256 and put some 1 char as the flag. Then you could recover the flag by doing
```python
from Crypto.Util.number import long_to_bytes

res = ... # put the digest here
res += ord(char) # char is the character you set as input
print long_to_bytes(res)
```
