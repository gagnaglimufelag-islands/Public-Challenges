#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct Levels
{
	int one;
	int two;
	int three;
	int get_flag;
}level;


void print_ascii()
{
	puts("    __   ________________   __________  __ __       __ _______ ____       ");
	puts("   / /  |__  /__  /_  __/  / ____/ __ \\/ // / _____/ //_/__  // __ \\      ");
	puts("  / /    /_ < /_ < / /    / /   / /_/ / // /_/ ___/ ,<   /_ </ /_/ /      ");
	puts(" / /______/ /__/ // /    / /___/ _, _/__  __/ /__/ /| |___/ / _, _/       ");
	puts("/_____/____/____//_/_____\\____/_/_|_|__/_/__\\___/_/_|_/____/_/_|_|_______ ");
	puts("/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/ ");
	puts("   / __ \\/ / / /  <  /__  /__  /__  /  |__  // | / / __ \\__  ______ _/ /_ ");
	puts("  / /_/ / / / /   / / /_ < /_ <  / /    /_ </  |/ / / / / / / / __ `/ __ \\");
	puts(" / _, _/ /_/ /   / /___/ /__/ / / /   ___/ / /|  / /_/ / /_/ / /_/ / / / /");
	puts("/_/ |_|\\____/   /_//____/____/ /_/   /____/_/ |_/\\____/\\__,_/\\__, /_/ /_/ ");
	puts("                                                            /____/        ");
	puts("============================================================================");
	puts("");
	(level.one == 1) ? puts("---------------------------> LEVEL ONE: PASSED! <----------------------------") : puts("---------------------------> LEVEL ONE: LOCKED <-----------------------------");
	(level.two == 1) ? puts("---------------------------> LEVEL TWO: PASSED! <----------------------------") : puts("---------------------------> LEVEL TWO: LOCKED <-----------------------------");
	(level.three == 1) ? puts("--------------------------> LEVEL THREE: PASSED! <---------------------------") : puts("---------------------------> LEVEL THREE: LOCKED <---------------------------");
	(level.get_flag == 1) ? puts("---------------------------> FLAG: EARNED! <---------------------------------") : puts("---------------------------> FLAG: LOCKED <----------------------------------");
}


void can_you_pass_me()
{
	char buffer[11];
	char *endptr;
	long password;

	printf("What is my favourite number: ");
	fgets(buffer, sizeof(buffer), stdin);
	password = strtol(buffer, &endptr, 10);
	
	if (password == 0xdeadbeef)
	{
		puts("[+] Ah, I see you're a man of culture as well.");
		level.one = 1;
		print_ascii();
	}
	else if (password > 0 && password != 0xdeadbeef)
	{
		puts("\n[!] Nope...Try again\n");
	}
	else if (password == 0)
	{
		puts("\nNumbers please!");

	}
}

void think_you_are_1337_now_huh()
{
	char buffer[4];
	int num = 0;
	printf("What is my new favourite number: ");
	fgets(buffer, sizeof(buffer), stdin);
	num = atoi(buffer);
	int xor_array[6] = {55, 245, 138, 125, 258, 33};

	for (short int i = 0; i < 6; i++)
	{
		num = num ^ xor_array[i];
	}
	
	if (num == 505)
	{
		puts("[+] You might be our next L33t H4x0r, keep it up!");
		level.two = 1;
		print_ascii();
	}
	else if (num > 0 && num != 505)
	{
		puts("[!] Hmmm...Are you really L33t enough?");
	}
}


void Are_you_a_wizard(int *pin)
{
	char buffer[6];
	int user_guess = 0;

	printf("What number am i thinking of: ");
	fgets(buffer, sizeof(buffer), stdin);
	user_guess = atoi(buffer);

	if (user_guess == *pin)
	{
		puts("[+] You're not a L33t H4x0r...You're a W1zArD!!!");
		level.three = 1;
	}
	else if (user_guess != *pin)
	{
		puts("\n[!] This ain't it, chief\n");
	}
}

int main()
{
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);


	level.one = 0;
	level.two = 0;
	level.three = 0;
	level.get_flag = 0;
	srand(time(NULL));
	int rand_num = rand() % 9000 + 1000;
	print_ascii();

	while (level.get_flag != 1)
	{
		
		if (level.one != 1)
		{
			can_you_pass_me();
		}
		else if (level.one == 1 && level.two != 1)
		{
			think_you_are_1337_now_huh();
		}
		else if (level.one == 1 && level.two == 1 && level.three != 1)
		{
			Are_you_a_wizard(&rand_num);
		}
		else if (level.one == 1 && level.two == 1 && level.three == 1)
		{
			level.get_flag = 1;
			print_ascii();
		}
	}

	if (level.get_flag == 1)
	{
		FILE *pfile;
		char flag[60];

		if ((pfile = fopen("flag.txt", "r")) == NULL)
		{
			printf("Error opening file 'flag.txt'");
			exit(-1);
		}
		else
		{
			fscanf(pfile, "%s", flag);
			fclose(pfile);
			puts("\n[+] Well....You deserve it");
			puts("[+] Here you go\n");
			puts(flag);
		}
	}

	return 0;
}
