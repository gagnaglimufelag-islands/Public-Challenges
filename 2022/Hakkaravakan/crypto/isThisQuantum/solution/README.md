# It this quantum?

## Overview

We are given an oracle which first generates a random prime $p$ and sends it to us. Then it takes in a string, hashes it, turns it into a integer $h$, and then computes $ct = flag * 2^h \pmod{p}$. The server sends back the first 48 bits of $ct$. We can find $h$ by hashing the string we send.

So we have to find $flag \pmod{p}$ given a (very bad) approximation of $flag * 2^h \pmod {p}$. This is the poster child of a problem known as the [hidden number problem](https://crypto.stanford.edu/~dabo/pubs/abstracts/dhmsb.html) (HNP for short). Usually when we have a approximation of something modulo some number $m$, we can usually turn that into finding a small (small as in containing few digits) solution modulo $m$. Which in turn can usually be converted to finding a small basis in a lattice (formally, this is called the shortest vector problem (SVP))

## Solving SVP

To solve an instance of a SVP problem like this one we first construct a basis spanning the solution where the solution is "small". Then we use LLL lattice reduction to get a small basis. Then be use Babai's nearest plane algorithm to find the closest solution vector to the basis given the vector of $ct$

The amount of queries needed varies but $2\sqrt{\log_2 p} = 64$ is usually a safe bet however for this challenge we only need 23 queries.

Let $x_n$ be $2^{h_n} \pmod{p}$. The basis we will use is 
$$
\begin{pmatrix}
p && 0 && \cdots && 0 && 0 \\
0 && p && \cdots && 0 && 0 \\
\vdots && && \ddots \\
0 && 0 && \cdots && p && 0 \\
x_0 && x_1 && \cdots && x_n && 1/p \\
\end{pmatrix}
$$
This lattice clearly spans a vector containing $flag/p$ in the last position.

Let $u$ be the vector of leaks given to us by the oracle (with an extra 0 element at the end).  Now we can use the nearest plane algorithm to find the nearest plane to $u$ in the basis. When we multiply u[-1] by p we get the flag `A Lattice is post-quantum protocol's worst friend gg{whyDoTheyCallItOvenWhenYouOfInTheColdFoodOfOutHotEatTheFood?_5238f72133}`
