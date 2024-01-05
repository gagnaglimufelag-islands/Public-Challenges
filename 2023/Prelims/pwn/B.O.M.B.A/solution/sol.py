#!/usr/bin/env python3
from pwn import remote, process
import yaml
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

def menu(r, choice):
    r.recvuntil(b"6. Exit the Game\n")
    r.sendline(str(choice).encode())


def see_score(r):
    menu(r, 3)
    tmp = (r.recvuntil(b"points\n"))
    if "999" in str(tmp):
        return access_cheat(r)
    else:
        return None

def access_cheat(r):
    menu(r, 5)
    msg = r.recvuntil(b"\n")

    return str(msg)

def main(r):
    # Send the command to play the game
    menu(r, 1)

    for _ in range(9):
        # Print the level of difficulty
        # Initialize the grid for the current difficulty level
        # Loop until the game is won or lost
        while True:
            # Print the current state of the grid
            r.recvuntil(b"Where is the bomb ?\n").decode()
            # Get the user's input for the X and Y coordinates

            r.sendline(b'0')
            r.sendline(b'0')
            # Get the response from the challenge
            response = r.recvline()

            if b"You won. Noice." in response:
                # Print the final state of the grid and move on to the next difficulty level
                break

            # Print the updated state of the grid
        # Reset the game for the next difficulty level
        #see_score()
        if see_score(r) is None:
            menu(r, 1)

def solve(r):
    # reset the game
    menu(r, 4)

    # set the name
    menu(r, 2)
    r.sendlineafter('name:', b"Playah")

    see_score(r)
    main(r)
    flag = see_score(r)

    return flag


def test(host, port):
    r = remote(host, port)
    flag = solve(r)
    assert FLAG in flag, flag
    r.close()

if __name__ == '__main__':
    sh = process("./chal", cwd=f"{HERE}/src")
    print(solve(sh))
