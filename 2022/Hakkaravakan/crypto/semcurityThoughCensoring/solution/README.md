# Semcurity though censoring

## Overview

Essentially [https://twitter.com/ENOENT_/status/1374679885101285376?s=20](this) but more fun because participant wont need to OCR the image and wont need to parse the awful thing that is ASN.1

The main idea is that you are given a partially censored ed25519 ssh key and you have to recover the private key. The private key wont be password protected since that would make the challenge too guessy.

## SSH private key format

The OpenSSH key format is a bit unusual, since it is a custom format encoded in PEM (i.e. Custom format encoded in base64 plus header and footer). This website does a good job of explaining it: (This website)[https://coolaj86.com/articles/the-openssh-private-key-format/].

The format is similar to the usual DER/BER format, with the main difference being that it is a length-value encoding scheme instead of tag-length-value encoding scheme. Luckily, most of the length values have not been overwritten, making the parsing much easier much easier.

## Recovering the public and private key

We can see that parts of both the public key and the private key have been overwritten. Luckily, the OpenSSH key format contains 3 copies of the public key so we can just use the one that isn't corrupted. 

The 20 upper bits of the private key have been overwritten. Unfortunately, these are ed25519 keys, so there doesn't exist any fancy partially known private key attack to recover the entire private key since this is technically not the private key but the seed to generate the actual private key as described [here](https://en.wikipedia.org/wiki/EdDSA) so we just have to go though all $2^20$ possibilities.

Unlike ECDSA, it is quite a pain to [implement ed25519](https://www.rfc-editor.org/rfc/rfc8032) so we will just use the `ed25519` python library. A parallelized version of this is available in `sol.py` (namely in `brute()` and `test()`)

The flag is just the private key (or rather, the seed) wrapped in `gg{}`

FLAG: `gg{6821a11dcf49b27377fdcba9b596532ba55f66f7267ee890e62422b23f378796}`
