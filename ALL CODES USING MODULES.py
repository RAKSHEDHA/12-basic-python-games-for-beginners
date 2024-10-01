def play_quiz():
    print("Welcome to my game hubs quiz!")

    playing = input("Do you want to play? (yes/no): ")

    if playing.lower() != "yes":
        quit()

    print("Okay! Let's play :)")

    # Quiz Categories and Questions with Multiple Choices
    quiz_data = {
        "Science": [
            {
                "question": "What does CPU stand for?",
                "options": ["A) Central Processing Unit", "B) Central Print Unit", "C) Control Processing Unit", "D) None of the above"],
                "answer": "A"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["A) O2", "B) H2O", "C) CO2", "D) H2"],
                "answer": "B"
            },
            {
                "question": "What planet is known as the Red Planet?",
                "options": ["A) Venus", "B) Earth", "C) Mars", "D) Jupiter"],
                "answer": "C"
            },
            {
                "question": "What gas do plants absorb from the atmosphere?",
                "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Helium"],
                "answer": "B"
            },
            {
                "question": "What is the powerhouse of the cell?",
                "options": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Endoplasmic Reticulum"],
                "answer": "C"
            },
        ],
        "Geography": [
            {
                "question": "What is the capital of France?",
                "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
                "answer": "C"
            },
            {
                "question": "Which river is the longest in the world?",
                "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"],
                "answer": "B"
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "options": ["A) China", "B) Japan", "C) Thailand", "D) India"],
                "answer": "B"
            },
            {
                "question": "What is the largest desert in the world?",
                "options": ["A) Sahara", "B) Gobi", "C) Kalahari", "D) Arctic"],
                "answer": "A"
            },
            {
                "question": "Which continent is the Sahara Desert located in?",
                "options": ["A) Asia", "B) Africa", "C) North America", "D) Australia"],
                "answer": "B"
            },
        ],
        "History": [
            {
                "question": "Who was the first President of the United States?",
                "options": ["A) Abraham Lincoln", "B) Thomas Jefferson", "C) George Washington", "D) John Adams"],
                "answer": "C"
            },
            {
                "question": "In what year did World War II end?",
                "options": ["A) 1939", "B) 1945", "C) 1950", "D) 1960"],
                "answer": "B"
            },
            {
                "question": "Who discovered America?",
                "options": ["A) Marco Polo", "B) Christopher Columbus", "C) Ferdinand Magellan", "D) Leif Erikson"],
                "answer": "B"
            },
            {
                "question": "Who was known as the Iron Lady?",
                "options": ["A) Angela Merkel", "B) Margaret Thatcher", "C) Golda Meir", "D) Indira Gandhi"],
                "answer": "B"
            },
            {
                "question": "What ancient civilization built the pyramids?",
                "options": ["A) Romans", "B) Greeks", "C) Egyptians", "D) Aztecs"],
                "answer": "C"
            },
        ],
        "Mathematics": [
            {
                "question": "What is 2 + 2?",
                "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
                "answer": "B"
            },
            {
                "question": "What is the square root of 16?",
                "options": ["A) 2", "B) 4", "C) 6", "D) 8"],
                "answer": "B"
            },
            {
                "question": "What is 5 * 6?",
                "options": ["A) 30", "B) 25", "C) 20", "D) 35"],
                "answer": "A"
            },
            {
                "question": "What is the value of pi (to 2 decimal places)?",
                "options": ["A) 3.12", "B) 3.14", "C) 3.16", "D) 3.18"],
                "answer": "B"
            },
            {
                "question": "What is 15% of 200?",
                "options": ["A) 25", "B) 30", "C) 35", "D) 40"],
                "answer": "B"
            },
        ],
        "Literature": [
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["A) Mark Twain", "B) Charles Dickens", "C) William Shakespeare", "D) J.K. Rowling"],
                "answer": "C"
            },
            {
                "question": "What is the main character's name in 'Moby Dick'?",
                "options": ["A) Ahab", "B) Ishmael", "C) Queequeg", "D) Starbuck"],
                "answer": "A"
            },
            {
                "question": "Who is the author of '1984'?",
                "options": ["A) George Orwell", "B) Aldous Huxley", "C) Ray Bradbury", "D) F. Scott Fitzgerald"],
                "answer": "A"
            },
            {
                "question": "What is the first book of the Harry Potter series?",
                "options": ["A) Harry Potter and the Philosopher's Stone", "B) Harry Potter and the Chamber of Secrets", "C) Harry Potter and the Prisoner of Azkaban", "D) Harry Potter and the Goblet of Fire"],
                "answer": "A"
            },
            {
                "question": "Who wrote 'Pride and Prejudice'?",
                "options": ["A) Jane Austen", "B) Emily Brontë", "C) Mark Twain", "D) Charles Dickens"],
                "answer": "A"
            },
        ],
        "Art": [
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
                "answer": "C"
            },
            {
                "question": "What is the art of folding paper called?",
                "options": ["A) Origami", "B) Calligraphy", "C) Painting", "D) Sculpture"],
                "answer": "A"
            },
            {
                "question": "Who is known for the painting 'Starry Night'?",
                "options": ["A) Van Gogh", "B) Picasso", "C) Dali", "D) Matisse"],
                "answer": "A"
            },
            {
                "question": "What is the term for a three-dimensional work of art?",
                "options": ["A) Painting", "B) Sculpture", "C) Drawing", "D) Printmaking"],
                "answer": "B"
            },
            {
                "question": "What medium is used in watercolor painting?",
                "options": ["A) Oil", "B) Acrylic", "C) Water", "D) Pastel"],
                "answer": "C"
            },
        ],
        "Music": [
            {
                "question": "What is the highest male singing voice?",
                "options": ["A) Baritone", "B) Tenor", "C) Bass", "D) Soprano"],
                "answer": "B"
            },
            {
                "question": "Who is known as the King of Pop?",
                "options": ["A) Elvis Presley", "B) Michael Jackson", "C) Prince", "D) Justin Timberlake"],
                "answer": "B"
            },
            {
                "question": "What instrument has 88 keys?",
                "options": ["A) Violin", "B) Guitar", "C) Piano", "D) Flute"],
                "answer": "C"
            },
            {
                "question": "Who composed the 'Fifth Symphony'?",
                "options": ["A) Mozart", "B) Beethoven", "C) Bach", "D) Chopin"],
                "answer": "B"
            },
            {
                "question": "What genre is 'Bohemian Rhapsody'?",
                "options": ["A) Pop", "B) Rock", "C) Classical", "D) Jazz"],
                "answer": "B"
            },
        ]
    }

    print("Please choose a category:")
    categories = list(quiz_data.keys())
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")

    category_choice = int(input("Enter the number of your choice: ")) - 1
    if category_choice < 0 or category_choice >= len(categories):
        print("Invalid choice. Exiting the game.")
        return

    selected_category = categories[category_choice]
    print(f"You selected: {selected_category}")

    score = 0

    # Ask each question in the selected category
    for q in quiz_data[selected_category]:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Select the correct option (A, B, C, D): ").strip().upper()
        if answer == q["answer"]:
            print('Correct!')
            score += 1
        else:
            print("Incorrect! The correct answer was: " + q["answer"])

    # Display the final score
    total_questions = len(quiz_data[selected_category])
    print("\nYou got " + str(score) + " questions correct!")
    print("You got " + str((score / total_questions) * 100) + "%.")
    print("well done good job! ")
# Start the quiz
play_quiz() 

#MATH QUIZ
import random
import time

# Constants for the game
OPERATORS = ["+", "-", "*"]
EASY_RANGE = (1, 10)
MEDIUM_RANGE = (5, 15)
HARD_RANGE = (10, 20)
TOTAL_PROBLEMS = 10
MAX_WRONG_GUESSES = 3

# Function to generate a math problem based on difficulty level
def generate_problem(difficulty):
    if difficulty == 'easy':
        min_operand, max_operand = EASY_RANGE
    elif difficulty == 'medium':
        min_operand, max_operand = MEDIUM_RANGE
    else:  # hard
        min_operand, max_operand = HARD_RANGE

    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(OPERATORS)

    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

# Function to get the difficulty level
def get_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print("Invalid choice. Please choose easy, medium, or hard.")

# Main game function
def play_game():
    # Get difficulty level
    difficulty = get_difficulty()

    # Track wrong answers and score
    wrong = 0
    score = 0

    input("Press Enter to start!")
    print("----------------------")

    start_time = time.time()

    # Loop through math problems
    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem(difficulty)
        wrong_attempts = 0
        
        while True:
            guess = input(f"Problem #{i + 1}: {expr} = ")

            # Check if the player's guess is correct
            if guess.isdigit() and int(guess) == answer:
                print("Correct!")
                score += 10  # Add points for correct answers
                break
            else:
                print("Incorrect!")
                wrong += 1
                wrong_attempts += 1

            # Check if player has exceeded max wrong guesses
            if wrong_attempts >= MAX_WRONG_GUESSES:
                print(f"Too many wrong attempts! Moving on... The correct answer was {answer}.")
                break

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("----------------------")
    print(f"Nice work! You finished in {total_time} seconds!")
    print(f"Total wrong answers: {wrong}")
    print(f"Your score is: {score}/{TOTAL_PROBLEMS * 10}")

    # Feedback based on performance
    if score == TOTAL_PROBLEMS * 10:
        print("Excellent! You got all answers correct!")
    elif score > (TOTAL_PROBLEMS * 10) // 2:
        print("Good job! You got more than half correct.")
    else:
        print("Keep practicing! You'll improve.")

# Main loop to allow replay
while True:
    play_game()
    play_again = input("\nWould you like to play again (yes/no)? ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break

#SNAKE GAME
import random
import pygame

pygame.init()

width,height=600,600
game_screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(" Snake Game")

snake_x,snake_y = width/2, height/2
change_x,change_y=0,0

food_x,food_y=random.randrange(0, width)//10*10,random.randrange(0, height)//10*10


clock=pygame.time.Clock()

snake_body=[(snake_x,snake_y)]


def display_snake_and_food():
    global snake_x,snake_y,food_x,food_y
    snake_x = (snake_x + change_x)%width
    snake_y = (snake_y + change_y)%height

    if ((snake_x,snake_y) in snake_body[ 1:]):
        print("GAME OVER")
        quit()

    snake_body.append((snake_x,snake_y))


    if (food_x == snake_x and food_y== snake_y):
        food_x,food_y=random.randrange(0, width)//10*10,random.randrange(0, height)//10*10
    else:
        del snake_body[0]

    #game_screen.fill((0,0,0))
    game_screen.fill( (150, 150, 150))
    pygame.draw.circle(game_screen,(0, 0, 128),(food_x,food_y),6)
    for (x,y) in snake_body:
        #pygame.draw.rect(game_screen,(255,255,105),[x,y,10,10])
        pygame.draw.circle(game_screen,(255, 255, 102),(x,y),6)

    pygame.display.update()

while True:
    events=pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.QUIT
            quit()
        if(event.type == pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                change_x=-10
                change_y=0
            elif (event.key==pygame.K_RIGHT):
                 change_x=10
                 change_y=0
            elif (event.key==pygame.K_UP):
                 change_x=0
                 change_y=-10
            elif (event.key==pygame.K_DOWN):
                 change_x=0
                 change_y=10


        display_snake_and_food()
        clock.tick(15)

#TIC TAC TOE
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
#2048
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
#CHOOSE YOUR ADVENTURE
def start_adventure():
    name = input("Type your name: ")
    print("Welcome,", name, "to this adventure!")

    while True:
        answer = input(
            "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

        if answer == "left":
            left_path()
        elif answer == "right":
            right_path()
        else:
            print('Not a valid option. You lose.')

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for trying,", name)
            break

def left_path():
    answer = input(
        "You come to a river, you can walk around it or swim across. Type 'walk' to walk around and 'swim' to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and you lost the game.")
    else:
        print('Not a valid option. You lose.')

def right_path():
    answer = input(
        "You come to a bridge, it looks wobbly. Do you want to cross it or head back? (type 'cross' or 'back'): ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them? (yes/no): ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger, and they are offended, and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

# Start the adventure
start_adventure()

#SLOT MACHINE
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines:", *winning_lines)
    else:
        print("No winning lines this time.")
        
    return winnings - total_bet


def main():
    balance = deposit()
    while balance > 0:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    if balance <= 0:
        print("You ran out of money! Game over.")
    else:
        print(f"You left with ${balance}. Thanks for playing!")


main()

#GUESS NUMBER
import random

def number_guessing_game():
    print("Welcome to the Game Hub's Number Guessing Game !")

    # Ask the player if they want to play
    play = input("Do you want to play? (yes/no): ").lower()

    if play != 'yes':
        print("Okay, maybe next time! Exiting the game.")
        return

    # Choose difficulty level
    print("\nSelect Difficulty Level:")
    print("1. Very Easy (Range 1-5, Unlimited attempts)")
    print("2. Easy (Range 1-10, Unlimited attempts)")
    print("3. Medium (Range 1-50, Max 7 attempts)")
    print("4. Hard (Range 1-100, Max 5 attempts)")
    print("5. Very Hard (Range 1-200, Max 8 attempts)")
    print("6. Impossible (Range 1-1000, Max 10 attempts)")

    difficulty = input("Enter the number for the difficulty level (1, 2, 3, 4, 5, or 6): ")

    # Set range and number of allowed attempts based on the difficulty level
    if difficulty == '1':
        lower_bound = 1
        upper_bound = 5
        max_attempts = None  # Unlimited attempts for Very Easy
        print("\nYou selected VERY EASY mode.")
    elif difficulty == '2':
        lower_bound = 1
        upper_bound = 10
        max_attempts = None  # Unlimited attempts for Easy
        print("\nYou selected EASY mode.")
    elif difficulty == '3':
        lower_bound = 1
        upper_bound = 50
        max_attempts = 7  # Limited attempts for Medium
        print("\nYou selected MEDIUM mode.")
    elif difficulty == '4':
        lower_bound = 1
        upper_bound = 100
        max_attempts = 5  # Limited attempts for Hard
        print("\nYou selected HARD mode.")
    elif difficulty == '5':
        lower_bound = 1
        upper_bound = 200
        max_attempts = 8  # Limited attempts for Very Hard
        print("\nYou selected VERY HARD mode.")
    elif difficulty == '6':
        lower_bound = 1
        upper_bound = 1000
        max_attempts = 10  # Limited attempts for Impossible
        print("\nYou selected IMPOSSIBLE mode.")
    else:
        print("Invalid selection. Exiting the game.")
        return

    # Generate a random number to guess
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"\nI have selected a number between {lower_bound} and {upper_bound}. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.")
            break

        # Provide hints based on how close the guess is
        difference = abs(guess - number_to_guess)
        if difference <= 3:
            print("Hint: You're very close!")
        elif difference <= 10:
            print("Hint: You're close!")
        elif difference <= 20:
            print("Hint: You're getting there!")
        else:
            print("Hint: You're far off!")

        # Check if the maximum attempts are exceeded for medium, hard, very hard, or impossible mode
        if max_attempts is not None and attempts >= max_attempts:
            print(f"\nSorry, you've reached the maximum attempts ({max_attempts})! The correct number was {number_to_guess}.")
            break

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game()
    else:
        print("Thank you for playing!")

# Start the game
number_guessing_game()

#HANGMAN
import random

# List of words with hints
word_list = {
    "python": "A popular programming language.",
    "hangman": "A word guessing game.",
    "challenge": "Something that tests your abilities.",
    "development": "The process of developing something.",
    "programming": "The act of writing computer programs.",
    "interface": "A shared boundary across which two or more separate components of a computer system exchange information.",
    "algorithm": "A step-by-step procedure for solving a problem.",
    "variable": "A storage location paired with an associated symbolic name.",
    "function": "A block of code that only runs when it is called.",
    "syntax": "The set of rules that defines the combinations of symbols that are considered to be correctly structured programs."
}

max_attempts = 4  # Reduce the number of incorrect attempts to increase difficulty

def get_random_word_and_hint():
    word = random.choice(list(word_list.keys()))
    hint = word_list[word]
    return word, hint

def display_hangman(attempts):
    stages = [  # 4 stages for increased difficulty
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |   
           |   
           |
        """,
        """
           ------
           |    
           |    
           |   
           |   
           |
        """
    ]
    return stages[attempts]

def play_hangman():
    word, hint = get_random_word_and_hint()
    guessed_letters = []
    attempts = 0
    word_completion = ["_" for _ in word]
    
    print("Welcome to Hangman!")
    print("Hint: ", hint)
    
    while attempts < max_attempts:
        print(display_hangman(attempts))
        print("Word:", " ".join(word_completion))
        print("Guessed letters:", " ".join(guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess not in word:
            print("Wrong guess!")
            attempts += 1
            guessed_letters.append(guess)
        else:
            print("Good guess!")
            guessed_letters.append(guess)
            for index, letter in enumerate(word):
                if letter == guess:
                    word_completion[index] = letter

        if "_" not in word_completion:
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print(display_hangman(attempts))
        print("Sorry, you've run out of attempts. The word was:", word)

# Main loop to allow replay
while True:
    play_hangman()
    play_again = input("Would you like to play again (yes/no)? ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break

#ROLL DICE
import random

# Function to roll the dice
def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Main game logic
def play_game():
    # Get number of players
    while True:
        players = input("Enter the number of players (2 - 4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print("Must be between 2 - 4 players.")
        else:
            print("Invalid, try again.")

    # Get custom maximum score
    while True:
        max_score = input("Enter the maximum score to win the game (e.g., 50): ")
        if max_score.isdigit():
            max_score = int(max_score)
            if max_score > 0:
                break
            else:
                print("Score must be greater than 0.")
        else:
            print("Invalid, try again.")

    # Get player names
    player_names = []
    for i in range(players):
        name = input(f"Enter Player {i + 1}'s name: ")
        player_names.append(name)

    # Initialize player scores
    player_scores = [0 for _ in range(players)]

    # Game loop
    while max(player_scores) < max_score:
        for player_idx in range(players):
            print(f"\n{player_names[player_idx]}'s turn has started!")
            print(f"Your total score is: {player_scores[player_idx]} \n")
            current_score = 0

            # Player's turn
            while True:
                should_roll = input("Would you like to roll (y/n)? ")
                if should_roll.lower() != "y":
                    break

                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a: {value}")

                print(f"Your score this round is: {current_score}")

            player_scores[player_idx] += current_score
            print(f"Your total score is now: {player_scores[player_idx]}")

            # Check if the player has won
            if player_scores[player_idx] >= max_score:
                break

    # Announce the winner
    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print(f"\n{player_names[winning_idx]} is the winner with a score of {max_score}!")

# Main loop to allow replay
while True:
    play_game()
    play_again = input("\nWould you like to play again (yes/no)? ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break

#TURTLE RACING
import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10. Try Again!')

def race(colors):
    turtles = create_turtles(colors)
    
    # Create the finish line
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.setpos(-WIDTH//2, HEIGHT//2 - 10)
    finish_line.pendown()
    finish_line.hideturtle()
    finish_line.forward(WIDTH)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

def display_winner(winner_color):
    # Display the winner
    winner_turtle = turtle.Turtle()
    winner_turtle.penup()
    winner_turtle.hideturtle()
    winner_turtle.setpos(0, 0)
    winner_turtle.write(f"The winner is the turtle with color: {winner_color}", align="center", font=("Arial", 20, "bold"))
    time.sleep(5)

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
display_winner(winner)

#RPS
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player1_choice, player2_choice):
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    if player1_choice == player2_choice:
        return "tie"
    elif win_conditions[player1_choice] == player2_choice:
        return "player1"
    else:
        return "player2"

def play_against_computer(player_name, max_attempts=3):
    player_score = 0
    computer_score = 0
    attempts = 0

    while attempts < max_attempts:
        # Player chooses rock, paper, or scissors
        player_choice = input(f"\n{player_name} (Player) - Enter your choice (rock, paper, scissors): ").lower()

        # Validate player's choice
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Computer chooses rock, paper, or scissors
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine the outcome
        result = determine_winner(player_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "player1":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Show the current score
        attempts += 1
        print(f"\nScore: {player_name} {player_score} - Computer {computer_score} (Attempt {attempts}/{max_attempts})")

    # Final results after max_attempts
    print("\nGame Over!")
    if player_score > computer_score:
        print(f"{player_name} wins the game with a score of {player_score} to {computer_score}!")
    elif player_score < computer_score:
        print("Computer wins the game with a score of {computer_score} to {player_score}!")
    else:
        print("It's a tie game!")

def play_multiplayer(player1_name, player2_name, max_attempts=3):
    player1_score = 0
    player2_score = 0
    attempts = 0

    while attempts < max_attempts:
        # Player 1 chooses rock, paper, or scissors
        player1_choice = input(f"\n{player1_name}, enter your choice (rock, paper, scissors): ").lower()

        # Validate player 1 choice
        if player1_choice not in ["rock", "paper", "scissors"]:
            print(f"Invalid choice. {player1_name}, please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Player 2 chooses rock, paper, or scissors
        player2_choice = input(f"{player2_name}, enter your choice (rock, paper, scissors): ").lower()

        # Validate player 2 choice
        if player2_choice not in ["rock", "paper", "scissors"]:
            print(f"Invalid choice. {player2_name}, please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Determine the outcome
        result = determine_winner(player1_choice, player2_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "player1":
            print(f"{player1_name} wins this round!")
            player1_score += 1
        else:
            print(f"{player2_name} wins this round!")
            player2_score += 1

        # Show the current score
        attempts += 1
        print(f"\nScore: {player1_name} {player1_score} - {player2_name} {player2_score} (Attempt {attempts}/{max_attempts})")

    # Final results after max_attempts
    print("\nGame Over!")
    if player1_score > player2_score:
        print(f"{player1_name} wins the game with a score of {player1_score} to {player2_score}!")
    elif player1_score < player2_score:
        print(f"{player2_name} wins the game with a score of {player2_score} to {player1_score}!")
    else:
        print("It's a tie game!")

def rock_paper_scissors_game():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Ask the player if they want to play
        play = input("Do you want to play? (yes/no): ").lower()
        if play != 'yes':
            print("Okay, maybe next time! Exiting the game.")
            break

        # Ask for player names
        player_name = input("Enter your name: ").strip()
        game_mode = input("\nChoose game mode:\n1. Play against Computer\n2. Multiplayer\nEnter the number of your choice: ").strip()

        if game_mode == '1':
            play_against_computer(player_name)
        elif game_mode == '2':
            player2_name = input("Enter the name of Player 2: ").strip()
            play_multiplayer(player_name, player2_name)
        else:
            print("Invalid choice. Exiting the game.")

        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Exiting the game.")
            break

# Start the game
rock_paper_scissors_game()

