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
