#include <stdint.h>
#include <stdio.h>

#define POLYSIZE 10

/* sage: a
1739835343
sage: b
3479787127 */

typedef struct polynomial {
	uint64_t coeff[POLYSIZE];
	uint64_t modulus;
} polynomial;

void printPol(polynomial pol) {
	for (int x = 0; x < POLYSIZE; ++x) {
		if (x != 0) {
			printf(" + ");
		}
		printf("%llu*x^%d", pol.coeff[x], x);
	}
	printf(" defined modulo %llu\n", pol.modulus);
}

uint64_t evaluate(polynomial pol, uint64_t x) {
	unsigned __int128 result = pol.coeff[POLYSIZE - 1];
	for (int i = POLYSIZE - 2; i >= 0; --i) {
		result *= x;
		result += pol.coeff[i];
		result %= pol.modulus;
	}
	return (uint64_t)result;
}
