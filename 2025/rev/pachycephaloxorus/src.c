// Sol: https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'78'%7D,'Standard',false)XOR(%7B'option':'Hex','string':'56'%7D,'Standard',false)XOR(%7B'option':'Hex','string':'34'%7D,'Standard',false)XOR(%7B'option':'Hex','string':'12'%7D,'Standard',false)To_Hex('0x%20with%20comma',13)From_Hex('Auto')XOR(%7B'option':'Hex','string':'12'%7D,'Standard',false)XOR(%7B'option':'Hex','string':'34'%7D,'Standard',false)XOR(%7B'option':'Hex','string':'56'%7D,'Standard',false)XOR(%7B'option':'Hex','string':'78'%7D,'Standard',false)&input=Z2d7NGhlYWRvWE9SdXNfdzRzX3RoM19ncjM0dGUzdF9kMW4wfQ&oeol=FF

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned char flagoxorus[] = {
    0x6f,0x6f,0x73,0x3c,0x60,0x6d,0x69,0x6c,0x67,0x50,0x47,0x5a,0x7d,
    0x7b,0x57,0x7f,0x3c,0x7b,0x57,0x7c,0x60,0x3b,0x57,0x6f,0x7a,0x3b,
    0x3c,0x7c,0x6d,0x3b,0x7c,0x57,0x6c,0x39,0x66,0x38,0x75, 0x00
};

const unsigned char xor_keys[] = {
    0x12,
    0x34,
    0x56,
    0x78 
};


void decode(char* output_buffer, size_t buffer_len) {
    size_t data_len = sizeof(flagoxorus) - 1;

    if (buffer_len <= data_len) {
        if (buffer_len > 0) output_buffer[0] = '\0';

        return;
    }

    for (size_t i = 0; i < data_len; ++i) {
        unsigned char current_char = flagoxorus[i];

        for (int k = 4 - 1; k >= 0; --k) {
            current_char ^= xor_keys[k];
        }

        output_buffer[i] = current_char;
    }

    output_buffer[data_len] = '\0';
}

int main() {
    char flag[128];

    decode(flag, sizeof(flag));

    printf("The flag has been subjected to a formidable multi-quad-layer encryption!\n");
    printf("They say it's like a 4-headed beast of an encryption.\n");
    printf("Unravel the layers and find the prehistoric prize!\n");
    printf("\nBe warned: even the mighty Nsaxorus has yet to defeat this mighty beast!\n");

    char user_guess[128];

    printf("\nEnter flag: ");
    if (scanf("%127s", user_guess) != 1) {
        fprintf(stderr, "Wrawrror reading input.\n");

        return 1;
    }

    if (strcmp(user_guess, flag) == 0) {
        printf("Correct! The unthinkable has come to happen, Pachycephaloxorus has been defeated!\n");
    } else {
        printf("Incorrect. The highly encrypted layers remain unpeeled. Check your keys and their sequence!\n");
    }

    return 0;
}
