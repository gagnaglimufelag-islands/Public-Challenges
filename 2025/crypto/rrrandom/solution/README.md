# Rrrandom
We are given a server where you can either get encrypted random values or the encrypted flag padded with random values.

Looking at the encryption mechanism `pow(r, e, n)`, we can see that it looks like RSA, so in order to solve it we first need to figure out what `n` is.

After some googling you might stumble upon the following site

https://cryptohack.gitbook.io/cryptobook/untitled/recovering-the-modulus

which shows how to recover n given 2 pairings of the plaintext and ciphertext, which we can get from sending `n` twice to the server.

Now that we know n, we need to figure out how to recover the flag.
Luckily for us there is a well known way to recover the common message given two ciphertexts if the padding is small enough, which uses coppersmiths small roots to extract the common message. 

One implementation of this attack can be found in the following link

https://github.com/pwang00/Cryptographic-Attacks/blob/master/Public%20Key/RSA/coppersmith_short_pad.sage

Using these two methods you can recover the flag

`gg{How_to_s0lve_Crypto?_Us3_LLL.}`
