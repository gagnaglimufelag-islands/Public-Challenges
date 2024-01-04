# Writeup

We are given an oracle which gives us a polynomial 34 roots. 33 of them are random roots and 1 of them is a character of the flag at some index of our choosing.

We can easily recover all the roots by trying all possible roots (i.e. all characters in `alphabet`).

If we recover the roots of two different polynomials (at the same index) and find which roots they share in common, the flag character root will remain and the other roots have a 50% chance of remaining. Do this enough times and the only root remaining will be the flag character.

Do this for all indices and we get the flag.

```
gg{411_Of_tH3_6iRD5_d13D_In_1986_du3_tO_r394n_k111In9_tH3M_1be5ecffa}
```
