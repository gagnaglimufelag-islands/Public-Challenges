#include <stdio.h>
#include <stdlib.h>

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	char password[16];
	int win = 0;

	printf("Enter the password! ");
	gets(password);
	
	if (win == 0x1337) {
		system("cat flag.txt");
		return;
	}
	
	printf("Wrong password %s!\n", &password);
}
