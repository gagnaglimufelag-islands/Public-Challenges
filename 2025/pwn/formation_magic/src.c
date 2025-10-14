// Challenge Name: Formation Magic
// Solve: for i in $(seq 30); do echo %$i\$s | ./bin/three; done | grep "The Oracle chants"
// then use that as the key to get the real flag
//
// NOTE: we need to compile this with a placeholder secret that is handed out as part of the challenge
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char* oracle_art =
"         _______________\n"
"    ()==(              (@==()\n"
"         '______________'|\n"
"           |             |\n"
"           | Ancient     |\n"
"           |  scroll     |\n"
"           |   of        |\n"
"           |    the      |\n"
"           |     flags   |\n"
"         __)_____________|\n"
"    ()==(               (@==()\n"
"         '--------------'\n";

void reveal_ancient_scroll() {
    FILE *fp;
    char flag_buffer[256];

    fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        printf("\nThe Oracle frowns. 'The Ancient Scroll (flag.txt) is missing from my sanctum!'\n");
        fflush(stdout);

        return;
    }

    printf("\nThe Oracle nods. 'You have proven your insight! Behold, the inscription on the Ancient Scroll:'\n");

    if (fgets(flag_buffer, sizeof(flag_buffer), fp) != NULL) {
        flag_buffer[strcspn(flag_buffer, "\n")] = 0;

        printf("%s\n", flag_buffer);
        fflush(stdout);
    } else {
        printf("'Hmm, the scroll appears blank... a mystery for another time!'\n");
        fflush(stdout);
    }

    fclose(fp);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    char secret_magic_word_on_stack3[64] = "this_is_a_folderholder"; 
    char user_incantation[256];
    char secret_magic_word_on_stack[64] = "super_secret_secret_that_cant_be_found"; 
    char guessed_magic_word[128];
    char secret_magic_word_on_stack2[64] = "this_is_a_cup_holder"; 

    printf("%s\n", oracle_art);
    printf("Welcome, seeker, to the Oracle of Formations!\n");
    printf("I possess a Secret Magic Word, hidden within the mists of memory.\n");
    printf("Only a true Formation Mage can divine it.\n");
    printf("Speak your incantation or forever hold your tongue:\n> ");

    if (fgets(user_incantation, sizeof(user_incantation), stdin) == NULL) {
        printf("The Oracle waits for an incantation...\n");

        return 1;
    }

    user_incantation[strcspn(user_incantation, "\n")] = 0;

    printf("\nThe Oracle chants: '");
    printf(user_incantation);
    printf("'\n");
    printf("...The echoes fade. The mists swirl.\n");

    printf("\nNow, young mage, if you have truly seen the unseen...\n");
    printf("Whisper the Secret Magic Word you have divined:\n> ");

    if (scanf("%127s", guessed_magic_word) != 1) {
        printf("The Oracle cannot hear your whisper...\n");

        return 1;
    }

    if (strcmp(guessed_magic_word, secret_magic_word_on_stack) == 0) {
        printf("\nIndeed! '%s' was the Secret Magic Word!\n", secret_magic_word_on_stack);

        reveal_ancient_scroll();
        fflush(stdout);
    } else {
        printf("\nAlas, '%s' is not the word I sense. The mists remain clouded.\n", guessed_magic_word);
        printf("Perhaps your incantation was flawed, or your vision unclear.\n");
        fflush(stdout);
    }

    printf("\nMay your future formations be fortunate!\n");
    fflush(stdout);

    return 0;
}
