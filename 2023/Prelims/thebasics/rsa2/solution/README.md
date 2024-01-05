# Really Simple Assignment 2
This time we are only given `n`, `e` and `c` so we can't easily decrypt the 
value like in the earlier challenge. However we also know that the flag
is four ASCII letters surrounded by `gg{}` which is easily crackable.

If we look at wikipedia again we can see that $c \equiv m^e \pmod{n}$. So we just
have to bruteforce a value such that `pow(m, e, n) == c` where `m` is our 
message, a.k.a. our flag. 

Now we have to perform the opposite action to `long_to_bytes`, that is 
`bytes_to_long`, which can be done easily in python3 like so `int(f"0x{hexlify(flag.encode()).decode()}", 16)`

After a short while of cracking we see the flag we see that the correct flag is
*gg{flag}* somewhat ironically.

