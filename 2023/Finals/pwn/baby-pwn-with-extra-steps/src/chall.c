#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <fcntl.h>

char buf[64];

int main() {
  setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

  int fd_one = 0;
  scanf("%d", &fd_one);

  srand(time(NULL));

  int sub = rand() % (0x9999 + 1 - 0x1001) + 0x1001;
  int fd = fd_one - sub;

  if (fd < 0x1001) {
    printf("No!\n");
    exit(1);
  }

  read((char)fd, buf, 64);

  if(!strcmp("The FitnessGram Pacer Test is a multistage...\n", buf)){
    char flag[256];
    int file = open("./flag.txt", O_RDONLY);

    if (file == -1) {
      puts("Failed to open flag, contact admin if remote");
      exit(1);
    }

    if (read(file, flag, 256) < 0) {
      puts("Failed to read flag, contact admin if remote");
      exit(1);
    };
    printf("%s\n", flag);
    exit(0);
  }
  return 0;
}

