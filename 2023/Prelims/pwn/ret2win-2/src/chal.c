#include <fcntl.h>
#include "stdio.h"
#include <unistd.h>
#include "stdlib.h"

void call_me_to_get_the_flag() {
	char flag[256];

	int f = open("./flag", O_RDONLY);
	if (f == -1) {
		puts("Failed to open flag. If this is on remote please contact an admin.");
		exit(1);
	}

	if (read(f, flag, 256) < 0) {
		puts("Failed to read flag. If this is on remote please contact an admin.");
		exit(1);
	};

	printf("Here is your flag: %s\n", flag);
}


int main() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	char name[10];
	
	puts("Hello, what is your name?");
	gets(name);
	printf("Hello %s\n", name);

	return 0;
}
