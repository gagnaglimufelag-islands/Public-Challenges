# Solution for Doncrypt
The vulnerability is that the encrypt.py program encrypts the ```Your Flag is ``` part with the flag. This allows us to use Don Coppersmiths known partial plaintext attack on the encrypted flag. First we assume that the first part of the message is ```Your Flag is 10an{``` then we do ```sage
P.<x> = PolynomialRing(Zmod(N), implementation = 'NTL')
pol = (message + x)^e - ciphertext
roots = pol.small_roots(epsilon=1/30)```
where N is the public key and e is the public exponent
```roots``` will contain a list of all possible roots (in out case there is only one root, that is, the flag)