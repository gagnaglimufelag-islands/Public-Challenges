import random
from Crypto.Util import number

import solution

N = 10

for n in range(N):
    base = number.getPrime(2**(n+1))
    exponent = random.randint(2, 10**(2*(n+1)))
    modulus = random.randint(2, base-1)
    result = pow(base, exponent, modulus)

    print('======== Test case %d/%d ========' % (n+1, N))

    answer = solution.solve(base, modulus, result)

    if answer == result:
        print('OK')
    else:
        print('Solution did not give the correct answer :(')
        print(f'{base}^{exponent} (mod {modulus}) =/= {answer}')
        print('Please try again')
        break
