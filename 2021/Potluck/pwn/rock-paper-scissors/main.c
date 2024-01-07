#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

// ASLR on
// gcc main.c -o rps -no-pie -fno-stack-protector

int game() {
	char sel[0xff];
	char cpuChoice[10];
	printf("Rock paper scissors?\n");
	gets(sel);
	char selection = tolower(sel[0]);
	if (selection == 'r') {
		strncpy(cpuChoice, "paper", 10);
	} else if (selection == 'p') {
		strncpy(cpuChoice, "scissors", 10);
	} else if (selection == 's') {
		strncpy(cpuChoice, "rock", 10);
	} else {
		printf("Invalid selection!\n");
		exit(0);
	}
	printf("You chose %s\n", sel);
	printf("Computer chose %s you lose!\n", cpuChoice);
	return 0;
}

int main(int argc, char* argv[]) {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	game();
	return 0;
}
