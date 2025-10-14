// Sol: 'strings -3', yep, that is it.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

const char* fun_facts[] = {
    "strings.exe: the original chit-chat app for binaries.",
    "Why did the string get an award? Because it was outstanding in its field of characters!",
    "This program is 100% organic, gluten-free, and contains many strings.",
    "gg{", // 3
    "My C strings are all null-terminated, just like my patience for debugging them.",
    "n0_", // 5
    "Heard about the string that went to therapy? It had too many attachment issues.",
    "If this binary was a book, `strings` would be the table of contents... and the spoilers.",
    "5tr1ng5_", // 8
    "The `strings` command: making binaries spill their guts since forever.",
    "I asked the binary for its secrets. It just gave me a long string of consciousness.",
    "4tt4ch3d}", // 11
    "Some strings are important, others are just here for the ASCII party.",
    "The secret to this challenge is hidden in one of these strings. Just kidding. Or am I?",
    "Rumor has it that the flag has been strung along.."
    "Sometimes I feel like a string in a binary world, just trying to find my place.",
    "If you think this string is long, wait until you see the one in my dreams.",
    "Hello, I am a string. I have no feelings, but if I did, I'd be very attached.",
    "This is not the string you are looking for... or is it?",
    "Parts of the flag missing? Ever had anyone 'man' explain 'strings' to you?",
    "All your string are belong to us."
    "A wild string appears! It's not very effective...",
    "The string manual is like a good book: full of twists, turns, and unexpected endings.",
    "Warning: Excessive use of the `strings` command may lead to premature flag discovery.",
};

int main() {
    srand(time(NULL));

    printf("This program has many strings attached. Some are more revealing than others.\n");
    printf("Perhaps a little interaction will shed some light?\n");
    printf("> ");

    char user_input_buffer[256];

    if (fgets(user_input_buffer, sizeof(user_input_buffer), stdin) != NULL) {
        user_input_buffer[strcspn(user_input_buffer, "\n")] = 0;

        if (strlen(user_input_buffer) > 0) {
            int fun_fact_id = rand() % (sizeof(fun_facts) / sizeof(fun_facts[0]));

            if (fun_fact_id == 3 || fun_fact_id == 5 || fun_fact_id == 8 || fun_fact_id == 11) {
                fun_fact_id += 1;
            }

            printf("\nAh, an inquisitive mind! You've chosen the path of interaction.\n");
            printf("Here's a thought for your troubles: \"%s\"\n", fun_facts[fun_fact_id]);
            printf("\n...and now, the program shall reflect on this profound interaction, indefinitely.\n");

        } else {
            printf("\nSilence? An interesting choice. The program continues, for now.\n");
        }

        fflush(stdout);
        while (1) {
            sleep(10);
        }
    } else {
        printf("\nNo input provided. The program's secrets remain within its structure..\n");
    }

    return 0;
}
