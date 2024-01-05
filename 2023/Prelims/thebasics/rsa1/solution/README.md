# Really Simple Assignment
This challenge is meant to introduce players to how you can encode text into 
numbers and vice versa.

The challenge description tells you that the numbers given are related to RSA.
When you look at the wikipedia page for RSA you quickly understand what `n`, `d`, and
`c` are used for. Now when we look at the decryption operation we can see that 
it is like so: $c^d \equiv m \pmod{n}$ which in python would be `pow(c, d, n)`.

So we've managed to decrypt the RSA ciphermessage given to us but we still se no
flag (`gg{.*}`). This is because we have decode the number into its bytes. This
operation is generally called `long_to_bytes`, but you can also do it in python3
using the `unhexlify` function coupled with `hex` like so `unhexlify(hex(m)[2:]).decode()`
and we have the flag: *gg{intro_to_the_basics_of_working_with_crypto_challs}*

