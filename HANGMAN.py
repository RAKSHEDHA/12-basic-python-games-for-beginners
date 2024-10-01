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
