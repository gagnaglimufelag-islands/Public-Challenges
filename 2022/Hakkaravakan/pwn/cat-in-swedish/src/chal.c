#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <limits.h>

#define READSIZE 128
#define TOTAL_QUESTIONS 10

int urandom_fd = -2;

void urandom_init() {
  urandom_fd = open("/dev/urandom", O_RDONLY);

  if (urandom_fd == -1) {
    int errsv = urandom_fd;
    printf("Error opening [/dev/urandom]: %i\n", errsv);
    exit(1);
  }
}

unsigned long gen_answer() {
  unsigned long buf_impl;
  unsigned long *buf = &buf_impl;

  if (urandom_fd == -2) {
    urandom_init();
  }

  read(urandom_fd, buf, sizeof(long));
  return buf_impl;
}

int kattis() {
    unsigned long correct_answers[TOTAL_QUESTIONS];
    for (int i = 0; i < TOTAL_QUESTIONS; i++) {
        correct_answers[i] = gen_answer();
    }

    unsigned long correct = gen_answer();
    char answer[READSIZE];

    printf("Warmup answer: ");

    fgets(answer, READSIZE, stdin);

    printf("Expected answer: %lu\n", correct);
    printf("You answered: ");
    printf(answer);
    printf("\n");

    printf("Starting challenge\nInput the correct numbers and get a flag!\n");
    for (int i = 0; i < TOTAL_QUESTIONS; i++) {
        unsigned long answer = 0;
        printf("> ");
        scanf("%lu", &answer);

        if (answer != correct_answers[i]) {
            printf("WRONG!\n");
            return 0;
        }
        printf("CORRECT!\n");
    }
    return 1;
}

void register_solved() {
    char flag[READSIZE];
    FILE *f = fopen("./flag.txt", "r");

    if (f == NULL) {
        printf("Flag file missing, please contact an administrator\n");
        exit(1);
    }

    fgets(flag, READSIZE, f);
    fclose(f);

    printf(" /\\_/\\\n");
    printf("( o.o )\n");
    printf(" > ^ <\n");
    printf("%s\n", flag);
    exit(0);
}

void intro() {
    printf(" ------------------------------------------------------------------------------ \n");
    printf("|                                                                              |\n");
    printf("| Cat In Swedish                                                               |\n");
    printf("| ==============                                                               |\n");
    printf("| An introductory competitive programming challenge for beginners, the         |\n");
    printf("| challenge doesn't even require input. All you have to do is output the       |\n");
    printf("| correct numbers according to the swedish cat.                                |\n");
    printf("|                                                                              |\n");
    printf("|                                                                              |\n");
    printf("| Input                                                                        |\n");
    printf("| =====                                                                        |\n");
    printf("| There is no input                                                            |\n");
    printf("|                                                                              |\n");
    printf("|                                                                              |\n");
    printf("| Output                                                                       |\n");
    printf("| ======                                                                       |\n");
    printf("| The correct random number N (0 <= N <= 2^32 - 1)                             |\n");
    printf("|                                                                              |\n");
    printf(" ------------------------------------------------------------------------------ \n");
    return;
}

int main(int argc, char* argv[]) {
	setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

    intro();
	int solved = kattis();

    if (solved) {
        register_solved();
    }
    printf("You've failed to input the correct numbers! No flag for you!");

	return 0;
}

