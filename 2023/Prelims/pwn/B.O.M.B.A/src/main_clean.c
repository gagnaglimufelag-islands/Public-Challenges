#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>



#define UNREVEALED "_x̼_"
#define BOMB "_B̼_"
#define MISSED "_o̼_"

#define SUPEREASY 100
#define EASY 200
#define MEDIUM 300
#define HARD 400
#define SUPERHARDCORE 500


typedef struct  {
    int x;
    int y;
    char state[5];
    int isBomb;
} LgcSquare;

typedef struct {
    char *name;
    int *score;
} PlyPlayer;

typedef struct{
    LgcSquare *squares;
    int size;
} LgcGrid;


void DplTraceGrid(LgcGrid *grid_ptr){

    char buffer[100];
    printf("    ");
    for(int i=0; i < (grid_ptr->size); ++i){
         snprintf(buffer, 100,"%-4d", i);
         printf(buffer);
    }
    printf("\n  ");
    for(int i=0; i < (grid_ptr->size); ++i){
        printf(" ___");
    }
    printf("\n");
    for(int i=0; i < grid_ptr->size; ++i){
        snprintf(buffer, 100,"%-3d", i);
        printf(buffer);
        for(int j=0; j < grid_ptr->size; ++j){
             snprintf(buffer, 100,"|%s", grid_ptr->squares[i*grid_ptr->size+j].state);
           printf(buffer);
        }
        printf("| \n");
    }
}


void LgcInitGrid(LgcGrid *grid){
    int current = 0;
    LgcSquare *squares = malloc((grid->size*grid->size) * (sizeof(*squares)));
    time_t t;
    srand((unsigned) time(&t));
    int bomb = rand() % (grid->size*grid->size);
    for(int length = 0; length < grid->size; length++ ){
         for(int width = 0; width < grid->size; width++){
               strncpy(squares[current].state, UNREVEALED,5);
            if(current == bomb){
                squares[current].isBomb = true;
            }
            else{
                squares[current].isBomb = false;
            }
             squares[current].x = width;
             squares[current].y = length;
             current++;
         }
     }
    grid->squares = squares;
}

LgcSquare * LgcGetSquare(LgcGrid *grid, int x, int y){
    int size = (grid->size)*(grid->size);
    for(int i=0; i < size;i++){
        if(grid->squares[i].x == x && grid->squares[i].y == y){
            return &grid->squares[i];
        }
    }
}


void win(){
    printf("You won. Noice.\n");
}

void gameover(){
    printf("Game Over\n");
    exit(0);
}

int LgcReveal(LgcGrid *grid, int x, int y){
    LgcSquare *square =  LgcGetSquare(grid, x, y);
    if(square->isBomb){
        strcpy(square->state, BOMB);
        win();
        return 1;
    }
    else{
        strcpy(square->state, MISSED);
    }
    return 0;
}


void PlySetPlayer(PlyPlayer *player, char * input){
    player->name = malloc(20);
    player->score = malloc(20);
    strcpy(player->name, input);
    *player->score = 0;
}


void PlyReset(PlyPlayer *player, int *difficulty){
    free(player->score);
    free(difficulty);
    free(player->name);
}

void  DplGetCoordinates(int *coords){
    char buffer[10];

    printf("Where is the bomb ?\nx>");

    scanf("%3s", buffer);
    coords[0] = (int) buffer[0] - '0';


    printf("y>");
    scanf("%3s", buffer);
    coords[1] = (int) buffer[0] - '0';


}


void DplMenu(){
        printf("1. Play the Game\n");
        printf("2. Set your name\n");
        printf("3. See your score\n");
        printf("4. Reset player\n");
        printf("5. Access the cheat engine\n");
        printf("6. Exit the Game\n");
}


void LgcIncreaseDifficulty(LgcGrid *grid, int * difficulty){
    difficulty[0] += 100;
    switch(difficulty[0]){
         case(SUPEREASY):
            grid->size= 1;
            break;
        case(EASY):
            grid->size= 2;
            break;
        case(MEDIUM):
            grid->size=3;
            break;
        case(HARD):
            grid->size=4;
            break;
        case(SUPERHARDCORE):
            grid->size=5;
            break;
    }
}



void logic(){


    LgcGrid grid;
    PlyPlayer player;
    int choice;
    int *difficulty = malloc(20);
    difficulty[0] = 0;
    LgcIncreaseDifficulty(&grid, difficulty);

    char buffer[400];
    int * coords = malloc(sizeof(int)*2);
    PlySetPlayer(&player, "player"); //init the player

    while(true){
        // printf("%p score : %d\n", player.score,player.score[0]);
        // printf("%p difficulty: %d\n", difficulty,difficulty[0]);
        // printf("%p name : %s\n", player.name,player.name);



        DplMenu();

        scanf("%3s", buffer);
        choice = (int) buffer[0] - '0';
        char name[200];

        switch(choice){
            case 1:
                LgcInitGrid(&grid);
                while(true){
                    DplTraceGrid(&grid);
                    DplGetCoordinates(coords);
                    if(LgcReveal(&grid, coords[0],coords[1])) {  break; };
                }
                player.score[0] += 11;
                LgcIncreaseDifficulty(&grid, difficulty);
                break;
            case 2:


                printf("Choose a new name: ");
                scanf("%30s", name);

                PlySetPlayer(&player, name);
                break;
            case 3:
                snprintf(buffer, 200, "score : %d\n", player.score[0]);
                printf(buffer);
                snprintf(buffer, 200, "difficulty: %d\n", difficulty[0]);
                printf(buffer);
                snprintf(buffer, strlen(player.name)+8, "name : %s\n", player.name);
                printf(buffer);
                snprintf(buffer, 200, "%s has %d points\n", player.name, *player.score);
                printf(buffer);
                break;
            case 4:
                PlyReset(&player, difficulty);
                break;
            case 5:
                if(*player.score == 999){
                    printf("here is the flag : 66{not_your_flag}\n");
                }else{
                    printf("w00p w00p you need 999 points to come here\n");
                }
                break;
            case 6:
                exit(0);
                break;
        };
    }
}


int main(int argc, char *argv[]){
	setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

    logic();
    exit(0);
}



