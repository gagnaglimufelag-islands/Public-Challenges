# Cat in swedish
The challenge presents you with a simple programming challenge for beginners.
All you have to do is output the correct number chosen at random 10 times!

However the random number is between `0` and `2^32 - 1` which is too large of space
to reliably guess correct 10 times in a row. What if we could leak the correct
answers?

## Solution
The programming challenge presents us with a warmup answer to prepare us for 
the randomly generated numbers to guess. When we take a guess we are presented
with the expected answer along with our answer.

If we start poking around and try entering `%x` we get back that our answer is
some hex number. This shows that there is likely a format string vulnerability.
This means we can leak the correct answers if they are pre-generated.

We can start by leaking numbers from the stack until we find the expected answer
we were presented with before. After that we can start leaking the next 10 answers
and see whether those are the pre-generated answers.

It is important to ensure that the leaked numbers are in the correct format,
which is decimal numbers between `0` and `2^32 - 1` a.k.a. `%lu`. 

Now when we leak enough to see the expected answer from before
and just one more integer and try inputting that one we can see that we get back 
the message that we have inputted the correct number!

All we have to do is leak the rest of the answers and input them to receive
the flag from the swedish cat.
