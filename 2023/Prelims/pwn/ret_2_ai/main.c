#include <stdio.h>
#include <stdlib.h>

#define READSIZE 128

void register_solved() {
    char flag[READSIZE];
    FILE *f = fopen("./flag.txt", "r");

    if (f == NULL) {
        printf("Flag file missing, please contact an administrator\n");
        exit(1);
    }

    fgets(flag, READSIZE, f);
    fclose(f);
    printf("%s\n", flag);
    exit(0);
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
		setvbuf(stderr, NULL, _IONBF, 0);

    int a[100], i, n, count = 0;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    for (i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i] == a[j])
                count = count + 1;
        }
    }
    if (count == n)
        puts("Yes");
    else {
        puts("No");
    }
    return 0;
}
