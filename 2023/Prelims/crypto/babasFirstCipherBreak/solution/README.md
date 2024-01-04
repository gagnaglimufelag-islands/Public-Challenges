# Writeup
In this challenge we are given the python script `encrypt.py` which encrypts any file given to it. Additionally we are given an encrypted flag in `flag.txt.enc`, a sick meme `whatYouEgg?HeStabsHim.png` and its encrypted counterpart `whatYouEgg?HeStabsHim.png.enc`.

When we open up `encrypt.py` we see that this is just a xor cipher with some wonky key generation. The key generation, although weird, is just repeated sha256 hashing with the salt "Watame Factory!". A important thing to note here is the amount of iterations, PBKDFs main function is to thwart brute force attempts, and they do so by taking a long time to compute. `passwordBasedKeyDerivationFunction` however, does not.

We see that although 999 bits are used to generate the password, only the first 16 are actually used since the rest is just cut off. This and the PBKDFs low iteration count means that we can just try all possible passwords as there are only $2^16$ of them.

To quickly filter out passwords we only decrypt the first 3 characters and compare then to "gg{" (the flag format). As I am not a fan of waiting, I decided to do this in parallel.

On my machine the multithreaded solution took 7s.

The author would appreciate if you took a moment to admire the sick double loss meme accompanying the challenge.

```
gg{Excuse me sir but is that original post you made right there loss? Now hold on, it might sound ridiculous but bare with me here. You see  there's 4 panels. Let's count them  1 2 3 4 panels! And you know what else has 4 panels ? That's right, loss does! But i'm not done yet, you see in the first panel there is 1 object  positioned slightly to the left. Should I even continue? I guess I will as you still don't understand. I should clarify this is a level 5 loss meme so I don't expect you to understand it. Anyways in the second panel there are 2 objects next to each other with one being slightly below the other. In the 3rd panel another 2 objects are present right next to each other. Finally, there are, yet again, 2 objects which form an L shape. Everything looks like it's adding up therefore it HAS to be loss!! You need to make it less obvious next time if you want it to be more funny._9f11cd31f7}
```
