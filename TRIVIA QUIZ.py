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
