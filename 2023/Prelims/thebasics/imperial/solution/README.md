# Imperial
The description mentions that the given text was encrypted using an ancient cipher named after Julius Caesar.
After some googling you will quickly discover that the cipher mentioned is called [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

There are multiple tools online which can decipher the given text for you, you can also easily implement your
own decipher in Python as a fun exercise.

If we go through the first few we can see that `x` should map to `g` like so:
```
x → y → z → a → b → c → d → e → f → g
```

Which means each character is shifted by 9 characters. So we can continue and see what we get:
```
x x { u r c v . . .

↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

g g { d a l e . . .
```

