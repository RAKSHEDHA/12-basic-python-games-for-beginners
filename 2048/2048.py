import random
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Constants
SIZE = 4
TARGET = 2048
TILE_SIZE = 110
TILE_PADDING = 20
WINDOW_PADDING = 20

TILE_IMAGES = {
    2: "D:/images/d.jpg",
    4: "D:/images/sh.jpeg",
    8: "D:/images/s.webp",
    16: "D:/images/n.jpeg",
    32: "D:/images/g.jpeg",
    64: "D:/images/d.jpg",
    128: "D:/images/sh.jpeg",
    256: "D:/images/s.webp",
    512: "D:/images/n.jpeg",
    1024: "D:/images/g.jpeg",
    2048: "D:/images/d.jpg"
}

def init_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def add_random_tile(board):
    empty_positions = [(i, j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]
    if empty_positions:
        i, j = random.choice(empty_positions)
        board[i][j] = 2 if random.random() < 0.9 else 4

def is_game_over(board):
    for row in board:
        if 0 in row:
            return False
    for i in range(SIZE):
        for j in range(SIZE):
            if (i < SIZE-1 and board[i][j] == board[i+1][j]) or (j < SIZE-1 and board[i][j] == board[i][j+1]):
                return False
    return True

def merge_tiles(tiles):
    merged = []
    skip = False
    for i in range(len(tiles)):
        if skip:
            skip = False
            continue
        if i < len(tiles) - 1 and tiles[i] == tiles[i+1]:
            merged.append(tiles[i]*2)
            skip = True
        else:
            merged.append(tiles[i])
    return merged

def move(board, direction):
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

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("Doraemon Polaroid 2048!")
        self.master.resizable(False, False)

        # --- Start Screen
        self.start_frame = Frame(self.master, bg="#add8e6")
        self.start_frame.pack(fill="both", expand=True)

        self.logo_path = "D:/images/doremon_logo.png"  # <- Change to your Doraemon logo image path
        if os.path.exists(self.logo_path):
            pil_logo = Image.open(self.logo_path).resize((300, 300))
            self.logo_img = ImageTk.PhotoImage(pil_logo)
            self.logo_label = Label(self.start_frame, image=self.logo_img, bg="#add8e6")
            self.logo_label.pack(pady=20)

        self.title_label = Label(self.start_frame, text="Doraemon 2048 Game", font=("Comic Sans MS", 24, "bold"), bg="#add8e6")
        self.title_label.pack(pady=10)

        self.score_label = Label(self.start_frame, text="Score: 0", font=("Comic Sans MS", 16), bg="#add8e6")
        self.score_label.pack(pady=5)

        self.start_button = Button(self.start_frame, text="New Game", font=("Comic Sans MS", 14, "bold"),
                                   bg="#ffffff", command=self.start_game)
        self.start_button.pack(pady=20)

        # --- Game Screen (hidden at first)
        self.game_frame = Frame(self.master, bg="#add8e6")

        self.board = init_board()
        self.images = {}
        self.score = 0

        canvas_size = (TILE_SIZE + TILE_PADDING) * SIZE + TILE_PADDING
        self.canvas = Canvas(self.game_frame, width=canvas_size, height=canvas_size, bg="#add8e6")
        self.canvas.pack(padx=WINDOW_PADDING, pady=WINDOW_PADDING)

        self.master.bind("<Key>", self.handle_key)

    def start_game(self):
        self.start_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        self.board = init_board()
        self.score = 0
        self.update_board()

    def update_score(self):
        total = sum(sum(row) for row in self.board)
        self.score = total
        self.score_label.config(text=f"Score: {self.score}")

    def update_board(self):
        self.canvas.delete("all")
        for i in range(SIZE):
            for j in range(SIZE):
                x1 = TILE_PADDING + j * (TILE_SIZE + TILE_PADDING)
                y1 = TILE_PADDING + i * (TILE_SIZE + TILE_PADDING)
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE
                value = self.board[i][j]

                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray", width=3)

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
        self.update_score()

    def handle_key(self, event):
        direction_map = {'Up': 'up', 'Left': 'left', 'Down': 'down', 'Right': 'right'}
        if event.keysym in direction_map:
            direction = direction_map[event.keysym]
            prev_board = [row[:] for row in self.board]
            move(self.board, direction)
            if prev_board != self.board:
                add_random_tile(self.board)
                self.update_board()

            if is_game_over(self.board):
                messagebox.showinfo("Game Over", "Oh no! Game Over. 😢")
                self.start_frame.pack(fill="both", expand=True)
                self.game_frame.pack_forget()
            elif any(TARGET in row for row in self.board):
                messagebox.showinfo("Congratulations!", "You reached 2048! 🎉")

def main():
    root = Tk()
    game = Game2048(root)
    root.mainloop()

if __name__ == "__main__":
    main()

