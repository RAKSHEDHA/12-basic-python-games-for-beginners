import random

# Function to print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check for a win
def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (draw)
def is_board_full(board):
    return all(space != " " for space in board)

# Function for player's turn
def player_move(board, player):
    while True:
        move = input(f"{player}, enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            if board[move] == " ":
                board[move] = "X" if player == player1 else "O"
                break
            else:
                print("That space is already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

# Function for computer's turn
def computer_move(board):
    available_spaces = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_spaces)
    board[move] = "O"

# Function to play the game
def play_game(player1, player2):
    board = [" " for _ in range(9)]
    scores = {player1: 0, player2: 0}
    mode = input("Enter 1 for single-player (against computer) or 2 for multiplayer: ")

    print_board(board)
    if mode == "1":
        while True:
            player_move(board, player1)
            print_board(board)
            if check_winner(board, "X"):
                print(f"{player1} wins!")
                scores[player1] += 1
                break
            elif is_board_full(board):
                print("It's a draw!")
                break

            print("Computer's turn...")
            computer_move(board)
            print_board(board)
            if check_winner(board, "O"):
                print(f"Computer wins!")
                scores[player2] += 1
                break
            elif is_board_full(board):
                print("It's a draw!")
                break

    elif mode == "2":
        current_player = player1
        while True:
            player_move(board, current_player)
            print_board(board)
            if check_winner(board, "X" if current_player == player1 else "O"):
                print(f"{current_player} wins!")
                scores[current_player] += 1
                break
            elif is_board_full(board):
                print("It's a draw!")
                break

            current_player = player2 if current_player == player1 else player1

    # Display scores
    print(f"\nScores:\n{player1}: {scores[player1]}\n{player2}: {scores[player2]}")

# Main loop to allow replay
while True:
    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O) or 'Computer' for single-player: ")
    
    play_game(player1, player2)
    
    play_again = input("Would you like to play again (yes/no)? ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
