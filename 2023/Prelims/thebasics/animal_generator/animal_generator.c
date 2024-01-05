#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

static const char NO_ONE[] = " run strings | ";

const char *first_words[8] = {
    "Daddy",
    "Long",
    "Forgetful",
    "Slightly",
    "Silly",
    "Pleasing",
    "Satanic",
    "Star-nosed"
};

const char *second_words[8] = {
    "NULL",
    "Snout",
    "Large",
    "Small",
    "Pink",
    "Little",
    "Crazy",
    "Hellbent"
};

const char *third_words[8] = {
    "Legs",
    "Human",
    "Ant",
    "Elephant",
    "Fishfingers",
    "Lumpsucker",
    "Fungus",
    "Wobbegong"
};

static const char FINDS_THIS[] = "grep flagformat}";

int main(int argc, char **args) {
    char answer[1];
    srand(time(0));

    const char *first = first_words[rand() % 7];
    const char *second = second_words[rand() % 7];
    const char *third = third_words[rand() % 7];

    printf("Welcome to the str...     err... I mean sentence generator!\n");
    printf("Do you want me to generate a sentence?\nEnter here [y/n]> ");
    scanf("%c", answer);

    static const char HOPE[] = "gg{always remember to";
    printf("Haha! You think you have a choice!? Here is your sentence, like it or not!\n");
    sleep(1);
    printf("Uh... takes a bit of time to generate...      hang on...\n");
    sleep(2);
    printf("\n%s %s %s\n", first, second, third);
    return 0;
}
