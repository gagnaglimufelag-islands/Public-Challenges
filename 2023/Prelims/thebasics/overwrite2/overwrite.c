#include <stdio.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);

    int secret = 0xdeadbeef;
    char your_secret[32];
    printf("Tell me your secret: ");
    gets(your_secret);
    if (secret == 0xbeefdead) {
        printf("Wow! gg{becoming_1337_hax0r_takes_time_and_now_youve_started_the_journey}\n");
    } else {
        printf("Yay more secrets! Now they are shared on Twitter and Mastodon.\n");
    }
}
