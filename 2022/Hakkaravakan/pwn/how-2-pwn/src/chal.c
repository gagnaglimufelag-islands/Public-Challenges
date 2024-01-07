#include "stdio.h"
#include "stdlib.h"


void win() {
	char flag[128];
	FILE *f = fopen("./flag.txt", "r");
	if (f == NULL) {
		printf("Missing flag, contact an admin if you are running this remotely");
		exit(0);
	}

	fgets(flag, 128, f);
	printf("Congratulations here is your flag: %s\n", flag);

	exit(0);
}


void init() {
	setvbuf(stdout, NULL, _IONBF, 0); 
	setvbuf(stdin, NULL, _IONBF, 0);
}


void *display_stack(void **stack) {
	void *ret = __builtin_return_address(1);

	stack--;
	// go through the stack until we find the return address
	while (*stack != ret) {
		printf("Stack addr: %p -> 0x%016llx\n", stack, *stack);
		stack++;
	}
	printf("Stack addr: %p -> 0x%016llx (stored return address)\n", stack, *stack);

	return (void *)stack;
}

void chal() {
	char buf[16];
	void *sp; // get rsp
	puts("Here is stack layout of the chal function.");
	puts("Your goal is to overwrite the return address");
	puts("With the address of the win function");
	printf("The win function is at %p\n\n", &win);

	sp = display_stack(&sp);
	printf("\nBuffer starts at %p\n", &buf);
	// maybe =8
	printf("%d bytes from buffer to return address\n\n", sp-(void *)&buf);


	puts("Reading input");
	gets(buf);

	puts("\n\nHere is the stack after reading your input");
	display_stack(&sp);


}

int main() {
	init();
	chal();
	printf("\nYou did not overflow the return address :( Try a longer input");
	return 0;
}
