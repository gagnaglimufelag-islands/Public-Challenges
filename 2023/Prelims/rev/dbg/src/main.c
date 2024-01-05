#include <stdio.h>
#include <string.h>
#include <ctype.h>


int main() {
    char verse1[] = "I'm a hacker, I'm a coder, I'm a cyber-savvy dude\n"
                    "I've got all the tools, and they're all really cool\n"
                    "From IDA to HXD, they're my secret weapons, see?\n"
                    "Without 'em, I'd be lost, just another wannabe\n\n";

    char chorus[] = "IDA, GHidra, radare, x32, x64, vim and HXD\n"
                    "They're the tools that set us free\n"
                    "We can hack, we can code, we can do anything we please\n"
                    "Thanks to these awesome tools, we're unstoppable, you see\n\n";

    char verse2[] = "When I'm working with binaries, IDA's my go-to friend\n"
                    "It's got all the features, from disassembly to debugging\n"
                    "GHidra's great for Java, it's a hacker's delight\n"
                    "With its reverse engineering, we can own any byte\n\n";

    char verse3[] = "Radare's like Swiss Army Knife, it's got it all inside\n"
                    "We can debug, we can patch, we can analyze with pride\n"
                    "x32 and x64, they're the CPUs we adore\n"
                    "With their power and speed, we can hack and explore\n\n";

    char verse4[] = "Vim's the editor we use, it's like a keyboard piano\n"
                    "With its commands and shortcuts, we're coding like Beethoven-o\n"
                    "And when we need to hex edit, HXD's the one\n"
                    "It's got all the features, from search to replace, it's fun\n\n";

    char outro[] = "So if you want to be a hacker, if you want to be a pro\n"
                   "Get yourself these tools, and watch your skills grow\n"
                   "You'll be unstoppable, you'll be the king of the hill\n"
                   "Thanks to IDA, GHidra, radare, x32, x64, vim and HXD, you will!\n";


    char result[50];
    memset(result, 0x0, 50);
    int result_len = 0;
    int index_list_verse[] = {6,0,22,22,10,193};
    int index_list_verse2[] = {64,25,13,3};
    int index_list_verse4[] = {4,1,96};


    for (int i = 0; i < 6; i++)
    {
	    result[i] = verse1[index_list_verse[i]];
	    result_len++;
    }
    result[1] = tolower(result[1]);
    strcat(result, "_in_p");
    result_len = result_len + 5;


    for (int i = 0; i < 4; i++)
    {
	    result[result_len+i] = verse2[index_list_verse2[i]];
    }
    strcat(result, "_");
    result_len = result_len + 5;

    for (int i = 0; i < 3; i++)
    {
	    result[result_len+i] = verse4[index_list_verse4[i]];
    }
    strcat(result, "ht");
    result_len = result_len + 5;

    char flag[result_len+7];
    memset(flag, 0x0, result_len+7);

    strcpy(flag, "gg{");
    strcat(flag, result);
    strcat(flag, "}");
    flag[sizeof(flag)-1] = '\0';

    // Print out the song lyrics
    printf("\n========================[ GG - 2023 ]==============================\n\nWelcome to GagnaGliman 2023, hope you have a blast and learn a ton\nHere Have a ChatGPT generated song:\n\n");
    printf("Verse 1:\n%s", verse1);
    printf("Chorus:\n%s", chorus);
    printf("Verse 2:\n%s", verse2);
    printf("Chorus:\n%s", chorus);
    printf("Verse 3:\n%s", verse3);
    printf("Chorus:\n%s", chorus);
    printf("Verse 4:\n%s", verse4);
    printf("Chorus:\n%s", chorus);
    printf("Outro:\n%s", outro);
    printf("\n========================[ GG - 2023 ]==============================\n\n");

    return 0;
}
