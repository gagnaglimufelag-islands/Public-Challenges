#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdbool.h>


#define FLAG_SIZE 64

bool win1 = false;
bool win2 = false;

void leap1() {
    win1 = true;
}

void leap2(unsigned int arg_check) {
    if (win1 && arg_check == 0xDEADBEEF) {
        win2 = true;
    }
    else if (win1) {
        printf("Getting there!");
    }
    else {
        printf("Failed Horribly!");
    }
}

void display_flag() {
    char flag[FLAG_SIZE];
    FILE *file;
    file = fopen("flag.txt", "r");
    if (file == NULL) {
        printf("'flag.txt' missing in the current directory!\n");
        exit(0);
    }

    fgets(flag, sizeof(flag), file);

    if (win1 && win2) {
        printf("%s", flag);
        return;
    }
    else {
        printf("Failed Horribly!");
    }
}

void get_name() {
  char buf[16];
  printf("Enter your name> ");
  return gets(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  get_name();
}
