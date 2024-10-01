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
