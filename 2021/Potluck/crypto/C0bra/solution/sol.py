#!/usr/bin/python3

"""
Intended solution:

By thoroughly reading the challenge description
you should have all the necessary information.
The first critical piece of information comes when
the description says: 1071 and 462 are my non-primes, shine away towards the GCD.

Here we have two numbers and something called a GCD.
GCD meaning Greatest Common Divisor, so taking the GCD
of both of these integer values gives us the number 21.

Now the first part is over with but you still have to solve the second part.
If you read the description meticulously you would have seen the second piece of information. Inverse multiplication is my jack of trade.
This immediately tells us that the long integer value in the mystery.txt file is multiplied and that we should reverse the multiplication which we can do by dividing the integer value with the number 21.

Now you should have the flag. But the flag is a one big number, again in the description you might have seen the name
of the young wise man. Askee meaning ASCII, Using any online ascii code to text converter (ex: https://www.dcode.fr/ascii-code)
Reveals the flag

10an{9R347357_C0Mm0n_D1v150R}
"""
def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
key = gcd(1071, 462)
cipher_text = 103928393125951432820365822475091724192991033009383148840232524625
ascii_flag = cipher_text // key
print(ascii_flag)
