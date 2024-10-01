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
