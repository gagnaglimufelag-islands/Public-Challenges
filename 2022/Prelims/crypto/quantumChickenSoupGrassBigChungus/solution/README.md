# Quantum Chicken Soup Grass Big Chungus

In this challenge we are tasked breaking a encryption system for secrets. Upon closer inspection we see that this is just asking us to find a discrete log using $p = 27046780809278300597$ and $g = 2$.

The first thing we notice is that $p$ is very small (~65 bits). Dlog algorithms (e.g. BSGS) usually run in $O(\sqrt{n})$ or faster which means that the discrete logarithm can be found in $2^{32}$ time which is essentially no time.

While the solution above works we can do better. The order of a finite field is $p-1$. If we factor $p-1$ we get 2 numbers that are ~32 bits long ($p$ is called $B$-smooth if none of its prime factors are bigger than $B$). This means that using Pohlig-Hellman we can find the discrete log in $\sqrt{2^{32}} = 2^{16}$ time. (Pohlig-Hellman works due to lagranges theorem and CRT)

Or you could just cheese this challenge by using Sage, pari/gp or CADO-NFS
