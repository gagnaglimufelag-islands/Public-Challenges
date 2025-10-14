import random
import os
import time
import re
import warnings

from collections import Counter
from itertools import chain
warnings.filterwarnings("ignore")

FLAG = os.getenv('FLAG', 'not_your_flag')
START_ROW = 'g'
ROWS = [chr(ord(START_ROW) + i) for i in range(10)]

def create_board():
    board = [[' ' for _ in range(10)]]
    board[0][1:] = list('0123456789')
    for i in range(10):
        board.append([chr(ord(START_ROW) + i)] + ['.'] * 10)
    return board

def mask_board(board):
    masked = [list(' 0123456789')]
    for row in board[1:]:
        masked_row = []
        for cell in row:
            if cell in {'b', 'X', *ROWS}:
                masked_row.append(cell)
            else:
                masked_row.append('.')
        masked.append(masked_row)
    return masked

def board_counter(board):
    return Counter(chain(*board))

def print_boards(comp_board, player_board):
    print("🧠 Enemy Waters".ljust(30) + "🌊 Your Fleet")
    masked_comp_board = mask_board(comp_board)
    for r in range(11):
        left = ' '.join(masked_comp_board[r])
        right = ' '.join(player_board[r])
        print(left.ljust(25) + '   ' + right)

def parse_pos(pos):
    row_char, col = pos[0], int(pos[1:])
    if not re.match(f'[{ROWS}', row_char):
        raise ValueError
    return ord(row_char) - ord(START_ROW) + 1, col + 1

def place_player_ship(board):
    print("👨‍✈️ Time to deploy your mighty vessel!")
    while True:
        try:
            pos = input("🔧 Enter starting position for your ship (e.g., g3): ").strip()
            direction = input("🧭 Vertical or horizontal (v/h): ").strip().lower()
            if len(pos) < 2 or direction not in ('v', 'h'):
                raise ValueError

            row,col = parse_pos(pos)

            if direction == 'h':
                if col > 7:
                    raise ValueError
                for i in range(3):
                    board[row][col + i] = 'B'
            else:  # vertical
                if row > 8:
                    raise ValueError
                for i in range(3):
                    board[row + i][col] = 'B'
            print("🚢 Ship deployed successfully!\n")
            break
        except KeyboardInterrupt:
            print("\n👋 Thanks for playing! Farewell, Admiral.")
            exit()
        except:
            print("⚠️ Invalid input or position. Try again.")

def place_computer_ship(board):
    s = random.randint(1,7)
    for i in range(3):
        board[0][s+i] = 'B'

def check_winning_condition(board):
    cnt = board_counter(board)
    if cnt['b'] == 3:
        return True

def player_turn(board):
    while True:
        try:
            pos = input("🎯 Where do you want to fire? (e.g., g3): ").strip()
            row,col = parse_pos(pos)

            cell = board[row][col]
            if cell in ('X', 'b'):
                print("🙅‍♂️ Already targeted. Try again!")
            elif cell == 'B':
                board[row][col] = 'b'
                print("💥 Direct hit!")
                break
            else:
                board[row][col] = 'X'
                print("💦 Splash! Just water.")
                break
        except KeyboardInterrupt:
            print("\n👋 Game aborted. Until next time, Captain.")
            exit()
        except:
            print("⚠️ Invalid input. Try again.")

def computer_turn(player_board):
    print("🧠 Enemy is plotting...")
    time.sleep(1.5)

    while True:
        row = random.randint(1, 10)
        col = random.randint(1, 10)
        if player_board[row][col] in ('X', 'b'):
            continue
        break
    if board_counter(player_board)['X'] > 2:
        for row, row_data in enumerate(player_board):
            if 'B' in row_data:
                col = row_data.index('B')
                break

    cell = player_board[row][col]
    if cell == 'B':
        player_board[row][col] = 'b'
        print(f"💣 Enemy fires at {chr(ord(START_ROW) + row - 1)}{col - 1}... and hits your ship! 😱")
    else:
        player_board[row][col] = 'X'
        print(f"💣 Enemy fires at {chr(ord(START_ROW) + row - 1)}{col - 1}... and misses! 😌")

def main():
    try:
        player_board = create_board()
        computer_board = create_board()

        print("🎮 Welcome to...\n")
        print("🛳️  **Terminal Battleship**  🚢")
        print("Let the sea battles begin!\n")

        place_player_ship(player_board)
        place_computer_ship(computer_board)

        while True:
            print_boards(computer_board, player_board)
            print("\n🫵 Your turn!")
            player_turn(computer_board)
            if check_winning_condition(computer_board):
                print("💣 You strike with unerring accuracy!")
                print("🛳️ The enemy's ship groans, breaks, and vanishes beneath the waves.")
                print("🎖️ You have triumphed against the impossible...")
                print(f"🏴 You claim your reward: {FLAG}")
                break


            print()
            computer_turn(player_board)
            if check_winning_condition(player_board):
                print("💥 The enemy has sunk your ship! 💀")
                print("🧠 Computer wins this round. But don’t worry, Admiral...")
                print("🌊 The sea always gives a second chance. Try again!")
                break

    except KeyboardInterrupt:
        print("\n👋 Game exited. Smooth sailing!")

if __name__ == "__main__":
    main()
