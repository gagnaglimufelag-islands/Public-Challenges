#include <stdlib.h>

char *chall(unsigned long val) {
    char *ans = malloc(9 * sizeof(char));
    for (int i = 0; i < 8; i++) {
        ans[7 - i] = (char)(val >> (8 * i));
    }
    ans[8] = '\0';
    return ans;
}
