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
