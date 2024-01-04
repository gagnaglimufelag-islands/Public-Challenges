import itertools
from secrets import choice
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import shuffle

def shuffled(s):
    x = list(s)
    shuffle(x)
    return x

with open('/usr/share/cracklib/cracklib-small', 'r') as f:
    WORDS = f.read().split()

N = 10

TEST_CASES = []

for _ in range(N):
    plaintext = choice(WORDS)
    key = bytes(itertools.islice(itertools.cycle(shuffled(plaintext.encode())), AES.block_size * 2))
    cipher = AES.new(key, AES.MODE_ECB)

    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

    TEST_CASES.append(b64encode(ciphertext).decode())

    # Print correct output for comparison later
    print(plaintext)

# Print separator to distinguish between correct output and output from user's solution
print('------------------------- SEP -------------------------')

import solution

for ciphertext in TEST_CASES:
    print(solution.decrypt(ciphertext))
