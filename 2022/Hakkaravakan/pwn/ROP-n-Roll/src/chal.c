#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include "funcs.h"


volatile char *username;
volatile unsigned int password;



void Print_Flag(volatile char *username_param, volatile unsigned int password_param)
{
	printf("Username: %s\n", username_param);
	printf("Password: %x\n\n", password_param);

	if (password_param != 0xDEADC0DE)
	{
		printf("[!] Not Authenticated!\n\n");
		return;
	}
	if (strcmp(username_param, "admin") != 0)
	{
		printf("[!] Not Authenticaed!\n\n");
		return;
	}
	
	
	
	FILE *fp;
	fp = fopen("./flag.txt", "r");
	if (fp == NULL){
		puts("Error reading file 'flag.txt'");
		puts("If you are seeing this on the remote server, please contact an admin.");	
	}

	int c;
	puts("[+] Successfully Authenticated...\n\n");
	while ((c = getc(fp)) != EOF){
		putchar(c);
		usleep(40000);

	}
	fclose(fp);
	exit(0);

}


int Gen_rand_num()
{
	return rand() % 256;
}

const char *Gen_rand_word()
{
	int index = rand() % 21;
	const char *words[] = { "election", "physics", "government", "dirt", "customer", "relation", "complaint", "basket", "football", "emotion", "outcome", "teaching", "shopping", "department", "midnight", "meat", "politics", "dealer", "reputation", "music" };
	return words[index];
}
const char *Create_secret()
{
	char secret[26];
	const char *secret_ret[26];
	memset(secret, '\0', sizeof(secret));
	int rand_index;
	char alphabet[27];
	memset(alphabet, '\0', sizeof(alphabet));
	int index = 0;
	char mid[6];
	memset(mid, '\0', sizeof(mid));
	int num1;
	int num2;
	char num1_str[6];
	char num2_str[6];
	char c;

	// Create alphabet array
	for (c = 'A'; c <= 'Z'; c++){
		alphabet[index] = c;
		index++;
	}

	// Assemble random five letters
	for (int i = 0; i < 5; i++){
		rand_index = rand() % 26;
		mid[i] = alphabet[rand_index];
	}

	num1 = Gen_rand_num();
	num2 = Gen_rand_num();
	
	// Copy first string to buffer
	strncat(secret, "s3cR3T_", sizeof(secret)-1);
	
	// Convert num1,num2 to str 
	snprintf(num1_str, sizeof(num1)+1, "%d", num1);
	snprintf(num2_str, sizeof(num2)+1, "%d", num2);

	// Create the secret (Append the strings)
	strncat(secret, num1_str, sizeof(secret)-1);
	strncat(secret, mid, sizeof(secret)-1);
	strncat(secret, num2_str, sizeof(secret)-1);
	strncat(secret, "_<3", sizeof(secret)-1);

	// return the secret
	*secret_ret = secret;	


	return *secret_ret;

}

void Guess_secret()
{
	char secret[26];
	memset(secret, '\0', sizeof(secret)-1);
	int ATTEMPTS = 0;
	int MAX_TRIES = 3;
	char Guess[256];
	strncat(secret, Create_secret(), sizeof(secret)-1);
	

	// Start of user input
	printf("Good Luck Guessing My secret :)\n\n");
	
	while (ATTEMPTS != MAX_TRIES)
	{
		printf("[%i/%i] Guess my secret: ", ATTEMPTS, MAX_TRIES);
		scanf("%255s", Guess);

		if (strcmp(Guess, secret) != 0)
		{
			printf("\n\nYour Guess: ");
			printf(Guess); // < -- Format string vulnerability
			printf("\nWrong secret!\n\n");
			ATTEMPTS++;
			if (ATTEMPTS == MAX_TRIES)
			{
				printf("Sorry, Your out of tries!\nThe Secret was: %s\n\n", secret);
				ascii_art();
				display_menu();
				
			}
		}
		else if (strcmp(Guess, secret) == 0 && ATTEMPTS != MAX_TRIES)
		{
			volatile unsigned int change_me;
			change_me = 0x1234;
			char buff[20];
			printf("\n[+] WOOOW WE MIGHT HAVE A REAL GENIUS HERE!\n[+] CAN YOU WORK THIS OUT?\n\n");
			printf("My variable before: %x\n\n", change_me);
			printf("Change me: ");
			scanf("%s", buff); // < -- Buffer overflow vulnerability
			printf("\nMy variable now: %x\n", change_me);
			if (change_me == 0xCAFEBABE){
				puts("[+] Well you deserve it\n");
				puts("[+] Let's upgrade tou to an admin\n");
				puts("[+] and give you the special token\n\n");
				username = "admin";
				password = 0xDEADC0DE;
				Print_Flag(username, password);
			}
			else
			{
				puts("Ahhh, nice try but that wasn't it\n");
				puts("[+] Returning to Menu...\n");
				sleep(2);
				ascii_art();
				display_menu();
				return;
			}
		}	
	}
	
}

void Enter_Debug(int passcode)
{
	int passcode_enc = ((2*(0xBEEF) ^ 0x16) * (passcode)) >> 0x10;
	
	if (passcode_enc == 1337){
		system("/bin/sh");
		exit(0);
	}
	else
	{
		printf("[-] Hmm...Looks like you don't have the right admin Token\n\n");
	}

}



void ascii_art()
{

	printf(R"""(
  _    _  ____  _    _  _____ ______    ____  ______    _____          _____  _____   _____ 
 | |  | |/ __ \| |  | |/ ____|  ____|  / __ \|  ____|  / ____|   /\   |  __ \|  __ \ / ____|
 | |__| | |  | | |  | | (___ | |__    | |  | | |__    | |       /  \  | |__) | |  | | (___  
 |  __  | |  | | |  | |\___ \|  __|   | |  | |  __|   | |      / /\ \ |  _  /| |  | |\___ \ 
 | |  | | |__| | |__| |____) | |____  | |__| | |      | |____ / ____ \| | \ \| |__| |____) |
 |_|  |_|\____/ \____/|_____/|______|  \____/|_|       \_____/_/    \_\_|  \_\_____/|_____/ 
                                                                                            
                                                                                            
	)""");

}




void start_game()
{

	srand(time(NULL));
	
	char choice[50];

	printf("#> ");
	scanf("%s", choice); // < -- Buffer Overflow Vulnerability


	if (strcmp(choice, "1") == 0)
	{
		printf("Here is Your Random Number: %i\n\n", Gen_rand_num());
	}
	else if (strcmp(choice, "2") == 0)
	{
		printf("Here is Your Random Word: %s\n\n", Gen_rand_word());
	}
	else if (strcmp(choice, "3") == 0)

	{
		Guess_secret();
	}
	else if (strcmp(choice, "4") == 0)
	{
		Enter_Debug(0);
	}
	else if (strcmp(choice, "5") == 0)
	{
		Print_Flag(username, password);
	}
	else if (strcmp(choice, "6") == 0)
	{
		exit(0);
	}
	else
	{
		printf("Not A Valid Option!\n\n");
	}

}

void display_menu()
{
	printf("\n[+] Username: %s\n\n\n", username);
	printf("Choose Your Adventure!\n\n");
	printf("[1] Generate A Random Number\n");
	printf("[2] Generate A Random Word\n");
	printf("[3] Guess My Secret\n\n");
	printf("------ ADMIN's ONLY ------\n");
	printf("[4] Enter Debug Mode\n");
	printf("[5] Print Debug Flag\n\n");
	printf("[6] Exit\n\n");

}

int main()
{
	// Initialize buffer stream
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);

	// Set Global Variables
	username = "padawan";
	password = 0xDEADBEEF;

	// Display Menu
	ascii_art();
	display_menu();
	
	while (true)
	{
		start_game();	
	}
	
	
	return 0;
}
