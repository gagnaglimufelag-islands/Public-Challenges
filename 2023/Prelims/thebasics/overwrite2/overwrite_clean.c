#include <stdio.h>

int main() {
    int secret = 0xdeadbeef;
    char your_secret[32];
    printf("Tell me your secret: ");
    gets(your_secret);
    if (secret == 0xbeefdead) {
        puts("Wow! falg{notyurfalg}");
    } else {
        printf("Yay more secrets! Now they are shared on Twitter and Mastodon.\n");
    }
}
