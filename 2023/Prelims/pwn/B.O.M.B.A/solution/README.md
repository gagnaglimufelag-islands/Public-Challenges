# B.O.M.B.A
In this challenge we are given the source code of the application. We can see that the code starts off by calling the `logic` which initializes the player object and difficulty. 

We find that we have a choice of playing the game, setting the player name, seeing the score, resetting the player, and finally we can see that if we choose to access the cheat engine and have exactly 999 points we will get the flag.

Whenever we win the game we gain 11 points. However 999 points isn't evenly divisible by 11 so we clearly can't just play the game enough times. Plus, the increasing difficulty would make it quite tedious to do.

The specific functions we are interested in are the ones that allocate the player and reset the player:
```C
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
```

We notice that the `difficulty` variable does not get reallocated and never gets reallocated in the program but does get used again. This means we have a use after free vulnerability.

So if we call the `PlyReset` (by pressing 4) function the `difficulty` variable will be freed, now if we call the `PlySetPlayer` (by pressing 2) function the score of the `player` struct will take up the memory slot previously owned by the `difficulty` variable.

This means that when we win the player score will increase by 111 points and 999 just so happens to be evenly divisible by 111.

```C
[...]
case 1:
    LgcInitGrid(&grid);
    while(true){
        DplTraceGrid(&grid);
        DplGetCoordinates(coords);
        if(LgcReveal(&grid, coords[0],coords[1])) {  break; };
    }
    player.score[0] += 11; // Increases the score by 11 points
    LgcIncreaseDifficulty(&grid, difficulty); // Increases the difficulty
    break;
case 2:
[...]

void LgcIncreaseDifficulty(LgcGrid *grid, int * difficulty){
    difficulty[0] += 100; // Increases the score by 100 points as player->score is now in the memory slot pointed to by difficulty
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
```

As an added side effect of this the difficulty never increases! This means we just have to play the game 9 times on the easiest difficulty and we can access the cheat engine.

```
1
    0   
   ___
0  |_x̼_| 
Where is the bomb ?
x>0
y>0
You won. Noice.
1. Play the Game
2. Set your name
3. See your score
4. Reset player
5. Access the cheat engine
6. Exit the Game
3
score : 999
difficulty: 999
name : watwat has 999 points
1. Play the Game
2. Set your name
3. See your score
4. Reset player
5. Access the cheat engine
6. Exit the Game
5
here is the flag : gg{W0W_y0u_Us3d_M3_Aft3r_Fr33}
1. Play the Game
2. Set your name
3. See your score
4. Reset player
5. Access the cheat engine
6. Exit the Game
6
```
