#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int win() {
	system("cat flag.txt");
};

char* answers[] = {"Computer says no.", "Joe mama.", "Indubitability.", "Supercalifragilisticexpialidocious!", "Yes.", "No.", "Terrible idea!", "Grape idea!"};
size_t size = sizeof(answers)/sizeof(answers[0]);

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	srand(time(NULL));
	
	char msg[64];

	printf("What is your question? ");
	read(0, msg, 0x64);

	printf("%s\n", answers[rand() % size]);
};
