# Boo The Game
<br>
<br>

# Summary
<br>

<h3><b>Intended solution</b></h3>

> By modifying the health value of the enemy to equal anything lower than the player's current health value will result in the player completing the level upon taking damage. Because the enemy takes damage by shootig the player we can decrease the health value of the enemy and make it lower than the player's current health for example let the enemies health equal `1` then upon taking damage the enemy is considered dead and we pass the level.
<br>

<br>

<h3><b>Unintended solution</b></h3>

> If we look at the strings in the binary we can quickly see that the game loads some interesting assets. The most useful one being the asset `c:\users\reverse\desktop\boothegame-dev\real_flag.png` so now if we load the game into any Hex Editor e.g (HxD) we can extract the loaded `PNG` file by copying the bytes of the png image then saving the bytes to a new file and opening it up reveals the flag. It's possible to also use a tool to extract the image file for example `Exepe Info`


<br>
<br>


# The challenge
> When loading into the first level of the game we can notice that our gun does not do any damage and what is really happening is that instead of us doing damage with our weapon we take damage by the enemy and the enemy loses health while doing so. The obvious problem here is that the enemy has plenty of health points while the player only has hundred points. So we can see that there is absolutely no way to win the game. Unless we use some cheats!

<br>
<br>


# Intended solution

Change the health of the enemy by using a memory editor e.g *Cheat Engine* or *PINCE*

- Attach to the game "BooTheGame.exe"
- Let the enemy lose some health
- ALT-TAB, scan the current enemy health
- Repeat steps 2-3 until only few addresses left
- Change the remaining addresses to the value `1`
- Take damage
- **Challenge completed**

<br>
<br>


# Unintended solution
 
- open the binary up in any hex editor
- search for the text `real_flag.png`
- Start copying from the magic bytes `%PNG` until `IEND`
- Copy bytes to a new file, save and open
- **Challenge completed**
