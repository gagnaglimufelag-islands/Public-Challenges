# Open Window 2
A continuation of the last open window challenge which has a main purpose of introducing the player
to XOR and some general rules to have in mind.

The lines of code of interest are the following:
```python
pass_bytes = password.encode()
result = [p ^ c for p, c in zip(pass_bytes, correct_bytes)]
return all(b == 0 for b in result)
```

Notice that each value from the `correct_bytes` array is XORed with each byte of the given string.
Next the function returns true if each XORed value is 0 otherwise it returns false. A rule to know
of when it comes to XOR is that `x ^ x == 0` which means that the flag is right in front of us in 
decimal. However there is one value in the array that is a bit of a gotcha: `3648 >> 5` but it 
won't bother you if you solve this in python like so:

```python
correct_bytes=[99, 48, 110, 103, 3648>>5, 52, 116, 117, 108, 97, 116, 49, 48, 110, 115, 33, 49, 33, 49, 33, 49, 33, 95, 110, 48, 119, 95, 117, 95, 107, 110, 48, 119, 95, 120, 48, 114, 95, 110, 48, 119, 95, 117, 114, 95, 114, 51, 52, 100, 121, 95, 116, 111, 95, 98, 51, 95, 97, 95, 114, 51, 118, 101, 114]
print("".join([chr(x) for x in correct_bytes]))
```

Which will give the flag `c0ngr4tulat10ns!1!1!1!_n0w_u_kn0w_x0r_n0w_ur_r34dy_to_b3_a_r3ver`, now you just
have to put `gg{}` around it.
