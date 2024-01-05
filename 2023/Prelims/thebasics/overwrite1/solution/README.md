# Overwrite Me
We are given the following source code:

```C
#include <stdio.h>

#define NAMESIZE 32

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);

    int secret = 0xdeadbeef;
    char your_secret[NAMESIZE];
    printf("Tell me your secret: ");
    gets(your_secret);
    if (secret == 0x464C4147) {
        printf("Wow! Here's your flag: falg{notyurfalg}\n");
    } else {
        printf("Successfully shared on Twitter!\n");
    }
}
```

If you try and compile the C code yourself, you will notice a warning saying 
the following:

> warning: the `gets` function is dangerous and should not be used.

Now when we google `gets` and research this a bit further we quickly learn about
something called *buffer overflow*, from there we might stumble upon an article
called *smashing the stack for fun and profit*. 

After reading the article we are well versed in the stack, endianness and buffer
overflow vulnerabilities and why they are bad.

So we try input a long string of *GALF* like so:

```
Tell me your secret: GALFGALFGALFGALFGALFGALFGALFGALFGALFGALFGALFGALFGALFGALFGALFGALFGALFGALFGALF
Wow! Here's your flag: gg{now_you_know_how_to_overwrite_stack_variables}
```
