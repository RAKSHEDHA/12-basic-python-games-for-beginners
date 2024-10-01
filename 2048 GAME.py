import random
import os
import sys

# Constants for the game
SIZE = 4
TARGET = 2048

# Initialize the game board with empty spaces
def init_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    add_random_tile(board)
    add_random_tile(board)
    return board

# Add a random tile (2 or 4) to a random empty position
def add_random_tile(board):
    empty_positions = [(i, j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]
    if empty_positions:
        i, j = random.choice(empty_positions)
        board[i][j] = 2 if random.random() < 0.9 else 4

# Print the game board
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("\t".join(str(num) if num != 0 else '.' for num in row))
    print()

# Check if the game is over (no valid moves left)
def is_game_over(board):
    for row in board:
        if 0 in row:
            return False
    for i in range(SIZE):
        for j in range(SIZE):
            if (i < SIZE - 1 and board[i][j] == board[i + 1][j]) or (j < SIZE - 1 and board[i][j] == board[i][j + 1]):
                return False
    return True

# Move tiles in the specified direction
def move(board, direction):
    if direction == "up":
        for j in range(SIZE):
            temp = [board[i][j] for i in range(SIZE) if board[i][j] != 0]
            merged = merge_tiles(temp)
            for i in range(SIZE):
                board[i][j] = merged[i] if i < len(merged) else 0
    elif direction == "down":
        for j in range(SIZE):
            temp = [board[i][j] for i in range(SIZE - 1, -1, -1) if board[i][j] != 0]
            merged = merge_tiles(temp)
            for i in range(SIZE):
                board[SIZE - 1 - i][j] = merged[i] if i < len(merged) else 0
    elif direction == "left":
        for i in range(SIZE):
            temp = [board[i][j] for j in range(SIZE) if board[i][j] != 0]
            merged = merge_tiles(temp)
            for j in range(SIZE):
                board[i][j] = merged[j] if j < len(merged) else 0
    elif direction == "right":
        for i in range(SIZE):
            temp = [board[i][j] for j in range(SIZE - 1, -1, -1) if board[i][j] != 0]
            merged = merge_tiles(temp)
            for j in range(SIZE):
                board[i][SIZE - 1 - j] = merged[j] if j < len(merged) else 0

# Merge tiles in the current row or column
def merge_tiles(tiles):
    merged = []
    skip = False
    for i in range(len(tiles)):
        if skip:
            skip = False
            continue
        if i < len(tiles) - 1 and tiles[i] == tiles[i + 1]:
            merged.append(tiles[i] * 2)
            skip = True
        else:
            merged.append(tiles[i])
    return merged

# Main game loop
def main():
    board = init_board()
    print_board(board)

    while True:
        move_direction = input("Enter move (w/a/s/d for up/left/down/right) or 'q' to quit: ").lower()
        if move_direction in ['w', 'a', 's', 'd']:
            direction_map = {'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'}
            move(board, direction_map[move_direction])
            add_random_tile(board)
            print_board(board)

            if is_game_over(board):
                print("Game Over!")
                break

            if any(TARGET in row for row in board):
                print("Congratulations! You've reached 2048!")
                break
        elif move_direction == 'q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
