#include <stdio.h>
#include <stdlib.h>

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	char name[16];
	
	printf("Your id is %p\n", name);

	printf("Please enter your name! ");
	gets(name);

}
