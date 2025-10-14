# Source: https://github.com/jvdsn/crypto-attacks/tree/master
import os
import sys

from sage.all import ZZ
from sage.all import continued_fraction
from math import gcd
from math import isqrt

def factorize(N, phi):
    """
    Recovers the prime factors from a modulus if Euler's totient is known.
    This method only works for a modulus consisting of 2 primes!
    :param N: the modulus
    :param phi: Euler's totient, the order of the multiplicative group modulo N
    :return: a tuple containing the prime factors, or None if the factors were not found
    """
    s = N + 1 - phi
    d = s ** 2 - 4 * N
    p = int(s - isqrt(d)) // 2
    q = int(s + isqrt(d)) // 2
    return p, q if p * q == N else None

def attack(N, e):
    """
    Recovers the prime factors of a modulus and the private exponent if the private exponent is too small.
    :param N: the modulus
    :param e: the public exponent
    :return: a tuple containing the prime factors and the private exponent, or None if the private exponent was not found
    """
    convergents = continued_fraction(ZZ(e) / ZZ(N)).convergents()
    for c in convergents:
        k = c.numerator()
        d = c.denominator()
        if pow(pow(2, e, N), d, N) != 2:
            continue

        phi = (e * d - 1) // k
        factors = factorize(N, phi)
        if factors:
            return *factors, int(d)
### end source

from Crypto.Util.number import * 
import yaml
from base64 import b64decode
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "challenge.yml"))["flags"][0]

def test():
    n,e,enc = [int(x.split(' = ')[-1])for x in open('src/output.txt').read().split('\n')]

    p,q,d = (attack(n,e))
    flag = (long_to_bytes(pow(enc,d,n)))
    assert FLAG.encode() in flag, flag
    print(flag)

if __name__ == '__main__':
    test()
