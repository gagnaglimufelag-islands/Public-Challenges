#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

#define MAX_ENTRY_LENGTH 256
#define MAX_ENTRIES 20

char flag[MAX_ENTRY_LENGTH];  // Global variable to store the flag

void print_menu() {
    printf("Day 211 in the spacial capsule. \n what do you want to do today ?\n");
    printf("\n1. Write journal entry\n2. Read latest journal entry\n3. Quit\n> ");
    fflush(stdout);
}

void write_entry(char* entry) {
    printf("Write your journal entry: ");
    fflush(stdout);
    fgets(entry, MAX_ENTRY_LENGTH, stdin);

    if (strchr(entry, '\n')) {
        puts("Oops! The system detected inappropriate content.");
        exit(1);
    }
}

void read_entry(const char* entry) {
    printf("Journal entry:\n");
    printf(entry);
    fflush(stdout);
}

void read_flag() {
    int fd = open("/src/flag.txt", O_RDONLY);
    read(fd, flag, sizeof(flag));
    close(fd);
}

int main(int argc, char *argv[]){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    int choice;
    unsigned int entryCount = 0;
    char entries[MAX_ENTRIES][MAX_ENTRY_LENGTH];

    read_flag();

    puts("-*- Astronaut Journal -*-");
    fflush(stdout);

    while (1) {
        print_menu();
        fgets((char *)&choice, 4, stdin);
        choice = atoi((const char *)&choice);

        if (choice == 2) {
            if (entryCount)
                read_entry(entries[entryCount - 1]);
            else
                puts("No journal entries found!");
        }
        else if (choice == 3) {
            break;
        }
        else if (choice == 1) {
            if (entryCount >= MAX_ENTRIES) {
                puts("Log storage full. Cannot add more entries.");
                exit(1);
            }
            write_entry(entries[entryCount++]);
        }
        else {
            puts("Invalid input.");
        }
    }

    exit(0);
}
