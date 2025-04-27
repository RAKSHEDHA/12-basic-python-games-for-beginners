import random
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Constants for game
SIZE = 4  # The size of the game board (4x4 grid)
TARGET = 2048  # The target value to reach for game success
TILE_SIZE = 110  # Size of each tile
TILE_PADDING = 20  # Padding between tiles
WINDOW_PADDING = 20  # Padding around the window

# Mapping of tile values to their corresponding image file paths
TILE_IMAGES = {
    2: "D:/images/d.jpg",
    4: "D:/images/sh.jpeg",
    8: "D:/images/s.webp",
    16: "D:/images/n.jpeg",
    32: "D:/images/g.jpeg",
    64: "D:/images/do.jpg",
    128: "D:/images/di.jpeg",
    256: "D:/images/nm.jpg",
    512: "D:/images/nd.jpg",
    1024: "D:/images/jk.jpg",
    2048: "D:/images/t.jpg"
}

# Initializes a new empty game board
def init_board():
    # Create a 4x4 board initialized with zeroes
    board = [[0] * SIZE for _ in range(SIZE)]
    # Add two random tiles to start the game
    add_random_tile(board)
    add_random_tile(board)
    return board

# Adds a random tile (2 or 4) to a random empty position on the board
def add_random_tile(board):
    empty_positions = [(i, j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]
    if empty_positions:
        # Randomly select an empty position and add a tile (2 or 4)
        i, j = random.choice(empty_positions)
        board[i][j] = 2 if random.random() < 0.9 else 4

# Checks if the game is over by checking if there are no empty spaces and no possible moves
def is_game_over(board):
    # Check if there are any empty positions
    for row in board:
        if 0 in row:
            return False
    # Check if any adjacent tiles are the same (can be merged)
    for i in range(SIZE):
        for j in range(SIZE):
            if (i < SIZE-1 and board[i][j] == board[i+1][j]) or (j < SIZE-1 and board[i][j] == board[i][j+1]):
                return False
    return True

# Merges adjacent tiles that have the same value
def merge_tiles(tiles):
    merged = []
    skip = False
    for i in range(len(tiles)):
        if skip:
            skip = False
            continue
        if i < len(tiles) - 1 and tiles[i] == tiles[i+1]:
            merged.append(tiles[i]*2)  # Merge the tiles by doubling the value
            skip = True  # Skip the next tile because it was merged
        else:
            merged.append(tiles[i])
    return merged

# Moves the tiles on the board based on the direction
def move(board, direction):
    # Implementing logic for each possible direction (up, down, left, right)
    if direction == "up":
        for j in range(SIZE):
            temp = [board[i][j] for i in range(SIZE) if board[i][j] != 0]
            merged = merge_tiles(temp)
            for i in range(SIZE):
                board[i][j] = merged[i] if i < len(merged) else 0
    elif direction == "down":
        for j in range(SIZE):
            temp = [board[i][j] for i in range(SIZE-1, -1, -1) if board[i][j] != 0]
            merged = merge_tiles(temp)
            for i in range(SIZE):
                board[SIZE-1-i][j] = merged[i] if i < len(merged) else 0
    elif direction == "left":
        for i in range(SIZE):
            temp = [board[i][j] for j in range(SIZE) if board[i][j] != 0]
            merged = merge_tiles(temp)
            for j in range(SIZE):
                board[i][j] = merged[j] if j < len(merged) else 0
    elif direction == "right":
        for i in range(SIZE):
            temp = [board[i][j] for j in range(SIZE-1, -1, -1) if board[i][j] != 0]
            merged = merge_tiles(temp)
            for j in range(SIZE):
                board[i][SIZE-1-j] = merged[j] if j < len(merged) else 0

# Class that manages the game logic and UI using Tkinter
class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("Doraemon Polaroid 2048!")  # Set the title of the window
        self.master.resizable(False, False)  # Disable resizing of the window

        # --- Start Screen Setup ---
        self.start_frame = Frame(self.master, bg="#add8e6")  # Create the start screen frame
        self.start_frame.pack(fill="both", expand=True)

        # Load and display the Doraemon logo on the start screen
        self.logo_path = "D:/images/doremon_logo.png"
        if os.path.exists(self.logo_path):
            pil_logo = Image.open(self.logo_path).resize((300, 300))
            self.logo_img = ImageTk.PhotoImage(pil_logo)
            self.logo_label = Label(self.start_frame, image=self.logo_img, bg="#add8e6")
            self.logo_label.pack(pady=20)

        # Title and score labels for the start screen
        self.title_label = Label(self.start_frame, text="Doraemon 2048 Game", font=("Comic Sans MS", 24, "bold"), bg="#add8e6")
        self.title_label.pack(pady=10)

        self.score_label = Label(self.start_frame, text="Score: 0", font=("Comic Sans MS", 16), bg="#add8e6")
        self.score_label.pack(pady=5)

        # Button to start a new game
        self.start_button = Button(self.start_frame, text="New Game", font=("Comic Sans MS", 14, "bold"),
                                   bg="#ffffff", command=self.start_game)
        self.start_button.pack(pady=20)

        # --- Game Screen Setup (Hidden Initially) ---
        self.game_frame = Frame(self.master, bg="#add8e6")

        self.board = init_board()  # Initialize the game board
        self.images = {}  # Dictionary to hold images for tiles
        self.score = 0  # Initialize score

        canvas_size = (TILE_SIZE + TILE_PADDING) * SIZE + TILE_PADDING
        self.canvas = Canvas(self.game_frame, width=canvas_size, height=canvas_size, bg="#add8e6")
        self.canvas.pack(padx=WINDOW_PADDING, pady=WINDOW_PADDING)

        # Bind keyboard events for user input
        self.master.bind("<Key>", self.handle_key)

    def start_game(self):
        # Start the game by hiding the start frame and showing the game frame
        self.start_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        self.board = init_board()  # Reset the board
        self.score = 0  # Reset score
        self.update_board()  # Update the board display

    def update_score(self):
        # Calculate the total score by summing up all tiles
        total = sum(sum(row) for row in self.board)
        self.score = total
        self.score_label.config(text=f"Score: {self.score}")  # Update the score label

    def update_board(self):
        # Update the game board display
        self.canvas.delete("all")  # Clear the canvas
        for i in range(SIZE):
            for j in range(SIZE):
                # Calculate position for each tile
                x1 = TILE_PADDING + j * (TILE_SIZE + TILE_PADDING)
                y1 = TILE_PADDING + i * (TILE_SIZE + TILE_PADDING)
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE
                value = self.board[i][j]

                # Draw tile background
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray", width=3)

                # Draw the value of the tile if it is non-zero
                if value != 0:
                    image_path = TILE_IMAGES.get(value)
                    if image_path and os.path.exists(image_path):
                        try:
                            pil_image = Image.open(image_path).resize((TILE_SIZE - 20, TILE_SIZE - 40))
                            tk_image = ImageTk.PhotoImage(pil_image)
                            self.images[(i, j)] = tk_image
                            self.canvas.create_image(x1 + TILE_SIZE//2, y1 + TILE_SIZE//2 - 10, image=tk_image)
                        except Exception as e:
                            print(f"Error loading image: {e}")

                    self.canvas.create_text(x1 + TILE_SIZE//2, y2 - 10, text=str(value),
                                            font=("Comic Sans MS", 16, "bold"), fill="black")
        self.update_score()  # Update the score after the board is updated

    def handle_key(self, event):
        # Handle user input for moving tiles
        direction_map = {'Up': 'up', 'Left': 'left', 'Down': 'down', 'Right': 'right'}
        if event.keysym in direction_map:
            direction = direction_map[event.keysym]
            prev_board = [row[:] for row in self.board]  # Make a copy of the current board
            move(self.board, direction)  # Move tiles based on user input
            if prev_board != self.board:
                add_random_tile(self.board)  # Add a random tile after each move
                self.update_board()  # Update the board display

            if is_game_over(self.board):
                # Show "Game Over" message if the game is over
                messagebox.showinfo("Game Over", "Oh no! Game Over. 😢")
                self.start_frame.pack(fill="both", expand=True)
                self.game_frame.pack_forget()
            elif any(TARGET in row for row in self.board):
                # Show "Congratulations" message if the target score is reached
                messagebox.showinfo("Congratulations!", "You reached 2048! 🎉")

# Main function to start the game
def main():
    root = Tk()
    game = Game2048(root)  # Initialize the game
    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()
