#include <stdio.h>
#include <stdlib.h>


void print_ascii()
{
	 puts("\n/$$$$$$$                     /$$         /$$");
	 puts("| $$__  $$                    | $$       /$$$$");
	 puts("| $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$|_  $$    /$$$$$$");
	 puts("| $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/  | $$   /$$__  $$");
	 puts("| $$  | $$| $$  \ $$| $$  \ $$| $$$$$$/   | $$  | $$$$$$$$");
	 puts("| $$  | $$| $$  | $$| $$  | $$| $$_  $$   | $$  | $$_____/");
	 puts("| $$$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$ /$$$$$$|  $$$$$$$");
	 puts("|_______/  \______/  \______/ |__/  \__/|______/ \_______/\n");
}


int main() 
{
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);

	int guess;
	int correct_guesses = 1;
	srand(678485);
	
	print_ascii();
	puts("I'm thinking of 5 numbers between 1 and 1000.\n");
	
	while (correct_guesses < 6) 
	{
		printf("Enter your guess for number [ %d ] : ", correct_guesses);
		scanf("%d", &guess);
		
		if (guess == ((rand() % 1000) + 1)) 
		{
			printf("Correct!\n");
			correct_guesses++;
		}
		else if (guess < 1 || guess > 1000)
		{
			puts("Number is out of range!");
			return 0;
		}
		else 
		{
			puts("Incorrect.");
			return 0;
		}
	}

	if (correct_guesses == 6) 
	{
		printf("\nCongratulations! You guessed all 5 numbers in the correct order\n\n");
		FILE *pfile;
		char flag[60];
		if ((pfile = fopen("flag.txt", "r")) == NULL)
		{
			printf("Error opening file 'flag.txt'");
			return -1;
		}
		else
		{
			fscanf(pfile, "%s", flag);
			puts(flag);
			fclose(pfile);
		}
	}
	else 
	{
		puts("Sorry, you didn't guess all 5 numbers correctly.");
		return 0;
	}
	
	return 0;
}

