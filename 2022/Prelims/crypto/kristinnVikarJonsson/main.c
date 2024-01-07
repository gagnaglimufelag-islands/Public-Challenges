#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "polynomial.c"

int main() {
	uint64_t modulus = 1479986272511935021;
	char* FLAG = ""; // CENSORED
	int length = strlen(FLAG);
	if (length % 8 != 0) {
		fprintf(stderr, "Length of flag must be divisible by 8");
		return -1;
	}
	length /= 8;
	srand(NULL);
	polynomial pol = {.modulus = modulus, .coeff = {rand(),rand(),rand(),rand(),rand(),rand(),rand(),rand(),rand(),rand()}};
	printPol(pol);
	for (int x = 0; x < length; ++x) {
		uint64_t res = *((uint64_t*)(FLAG + 8*x));
		res = evaluate(pol, res);
		printf("part %d: %llu\n", x, res);
	}
	return 0;
}
