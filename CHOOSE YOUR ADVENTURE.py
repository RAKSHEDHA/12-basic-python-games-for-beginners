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
