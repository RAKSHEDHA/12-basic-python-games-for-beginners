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
