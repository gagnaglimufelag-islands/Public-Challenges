# Exclusivity
You are given an encrypted message in a file named `enc.txt` along with a python program which created that file.

When analyzing the python program we can see that the flag has been XORed with a single random byte and the result written into `enc.txt`.

This means you can go through each of the 256 bytes and XOR against the contents of `enc.txt`, once you get a message that starts with `gg{`, you will know that you got the correct byte.
