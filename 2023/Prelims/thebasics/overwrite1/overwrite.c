#include <stdio.h>

#define SECRETSIZE 32

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);

    int secret = 0xdeadbeef;
    char your_secret[SECRETSIZE];
    printf("Tell me your secret: ");
    gets(your_secret);
    if (secret == 0x464C4147) {
        printf("Wow! Here's your flag: gg{now_you_know_how_to_overwrite_stack_variables}\n");
    } else {
        printf("Successfully shared on Twitter!\n");
    }
}
