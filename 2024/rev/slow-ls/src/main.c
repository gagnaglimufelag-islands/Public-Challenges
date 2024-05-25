#include <stdio.h>
#include <unistd.h>


int main() {
    char input[300];
    int correct = 0;
    int sums[121] = {126, 164, 201, 142, 180, 197, 118, 194, 129, 74, 186, 199, 118, 190, 192, 72, 156, 185, 144, 148, 156, 71, 196, 173, 144, 180, 195, 118, 172, 188, 71, 196, 173, 127, 54, 197, 118, 190, 126, 118, 186, 129, 141, 148, 127, 118, 186, 179, 120, 174, 186, 144, 148, 182, 71, 182, 179, 118, 200, 189, 140, 148, 178, 72, 158, 188, 139, 148, 178, 71, 148, 194, 127, 56, 193, 118, 176, 175, 133, 192, 175, 131, 174, 199, 118, 180, 192, 118, 154, 199, 118, 166, 175, 133, 158, 173, 72, 190, 173, 142, 54, 195, 131, 158, 173, 121, 160, 173, 136, 192, 127, 139, 160, 173, 120, 148, 190, 120, 168, 188, 148};
    int tmp = 0;

    printf("Guess the password password: ");
    fgets(input, 150, stdin);

    printf("Checking password...\n");
    sleep(3);
    printf("Processing inputs...\n");
    sleep(3);
    printf("Hang on, this might take a while...\n");

    for (int i = 0; i < 121; i++) {
        sleep(3);
        if (i % 3 == 0) {
            tmp = input[i] + 23;
            if (tmp != sums[i]) {
                correct = 1;
            }
        } else if (i % 3 == 1) {
            tmp = (int)input[i] * 2 - 42;
            if (tmp != sums[i]) {
                correct = 1;
            }
        } else if (i % 3 == 2) {
            // tmp = (input[i] * 2 + 256) / 2 - 50;
            tmp = input[i] * 2;
            tmp = tmp + 256;
            tmp = tmp / 2 - 50;
            if (tmp != sums[i]) {
                correct = 1;
            }
        }
        sleep(5);
    }

    if (correct == 0) {
        printf("Correct!\n");
    } else {
        printf("Incorrect!\n");
    }
    return 0;
}
