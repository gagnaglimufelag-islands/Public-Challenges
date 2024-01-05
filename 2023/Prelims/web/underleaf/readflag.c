#include <stdio.h>
#include <unistd.h>

int main() {
	seteuid(0);
	setegid(0);
	setuid(0);
	setgid(0);
	char flag[500] = {0};

	FILE* f = fopen("/flag", "r");
	if (!f) {
		perror("Flag missing contact an admin.");
		return 1;
	}

	if (fread(flag, 1, 500, f) < 0) {
		perror("Failed to read flag contact an admin.");
		return 1;
	}
	puts(flag);
	fclose(f);
	return 0;
}