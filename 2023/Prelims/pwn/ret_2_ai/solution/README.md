# Ret2AI
The challenge is based on this [tweet](https://twitter.com/Trumpery45/status/1511101713805361152/photo/1)

The first `scanf` determines the size and it fails to check for overflows. You can set an `n` larger than the buffer to enduce a buffer overflow.

Now you can overwrite the instruction pointer with an integer which is the decimal equivalent of the address of the `ai` function
