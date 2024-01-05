#include "stdio.h"
#include "time.h"
#include <fcntl.h>
#include <unistd.h>
#include "stddef.h"
#include "stdlib.h"

int nums[6] = {};
int guesses[6] = {};
unsigned long seed = 0;


int getint() {
	char buf[0x10] = {};
	int len;
	if ((len = read(STDIN_FILENO, buf, sizeof(buf)-1)) <= 0) 
		return -1;

	if (buf[len-1] == '\n')
			len--;
	buf[len] = '\0';

	return atoi(buf);
}

void win() {
	char flag[256];
	int f = open("./flag", O_RDONLY);
	if (f == -1) {
		puts("Failed to open flag. If this is on remote please contact and admin.");
		exit(1);
	}
	if (read(f, flag, 256) < 0) {
		puts("Failed to read flag. If this is on remote please contact and admin.");
		exit(1);
	};
	printf("Here is your flag: %s\n", flag);
}

void lotto() {
	srand(seed);
	for (int i = 0; i < 6; i++) {
		nums[i] = rand() % 3274;
	}

	int index;
	for (int i = 0; i < 6; i++) {
		puts("What index are you guessing?");
		index = getint();
		puts("What number is it?");
		guesses[index] = getint();
	}

	for (int i = 0; i < 6; i++) {
		if (nums[i] != guesses[i]) {
			puts("You lost\n\n\n\n");
			return;
		}
	}
	win();
	return;
}

void init() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
};

int main() {
    init();
    seed = time(NULL);
	int num;
	puts("How many lottery tickets do you want?");
	num = getint();
	for (int i = 0; i < num; i++) {
		lotto();
	}
	return 0;
}
