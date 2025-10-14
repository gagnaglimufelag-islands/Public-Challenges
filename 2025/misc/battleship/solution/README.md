# battleship

Here we play a game of battleship against a cheating computer. The board is
stored as an 11x11 matrix, that includes row and column labels. The computer
uses this fact to "hide" its ship in the first row (row "f"), containing the
column labels.

Due to input validation, the player cannot choose to attack row f. However, the input validation uses the variable `ROWS` which as an array of strings to generate a regex

```
if not re.match(f'[{ROWS}', row_char):
```

meaning that the regex looks something like `[['g', 'h', ...]`. This means that, as well as matching the appropriate row letters, it also matches characters such as `'`, `,` and, crucially, `[`. When row letters are supplied, their position is calculated as `ord('g') - ord(char) + 1`, and since `ord('g') - ord('[') + 1` happens to be -11. Since we are dealing with an 11x11 matrix, in Python, that implies that -11 references the first row. We can, therefore, use the character `[` to attack the first row, and we have six guesses to identify the location of the computer's ship before the computer win. By guessing the first six columns of the first row, we have a very high chance of sinking the computer's ship. Therefore, we should be able to win the game within a few attempts.
