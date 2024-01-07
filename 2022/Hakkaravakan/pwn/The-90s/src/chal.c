#include <stdio.h>
#include <string.h>


char overflow[500];

int main(int argc, char *argv[])
{
	setbuf(stdout, NULL);
	setbuf(stdin, NULL);

	char input[500];

	printf("Magic Cookie: %p\n\n", input);
	printf("FEED ME: ");
	gets(input);
	strcpy(overflow, input);

	return 0;
}
