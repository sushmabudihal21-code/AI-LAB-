import tkinter as tk
from tkinter import messagebox
import random

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x450")
root.resizable(False, False)

# Game Variables
choices = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0

# Function to Play Game
def play(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    player_label.config(text=f"Player Choice: {player_choice}")
    computer_label.config(text=f"Computer Choice: {computer_choice}")

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"Player Score: {player_score}    Computer Score: {computer_score}"
    )

# Reset Game
def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    player_label.config(text="Player Choice: ")
    computer_label.config(text="Computer Choice: ")
    result_label.config(text="Choose Rock, Paper, or Scissors")
    score_label.config(text="Player Score: 0    Computer Score: 0")

# Heading
heading = tk.Label(
    root,
    text="Rock Paper Scissors Game",
    font=("Arial", 20, "bold")
)
heading.pack(pady=15)

# Instructions
instruction = tk.Label(
    root,
    text="Select your move",
    font=("Arial", 12)
)
instruction.pack()

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(
    button_frame,
    text="🪨 Rock",
    width=12,
    height=2,
    font=("Arial", 12),
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    button_frame,
    text="📄 Paper",
    width=12,
    height=2,
    font=("Arial", 12),
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(
    button_frame,
    text="✂️ Scissors",
    width=12,
    height=2,
    font=("Arial", 12),
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)

# Labels
player_label = tk.Label(root, text="Player Choice: ", font=("Arial", 13))
player_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 13))
computer_label.pack(pady=5)

result_label = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 16, "bold")
)
result_label.pack(pady=15)

score_label = tk.Label(
    root,
    text="Player Score: 0    Computer Score: 0",
    font=("Arial", 14)
)
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12, "bold"),
    command=reset_game
)
reset_btn.pack(pady=15)

# Run Application
root.mainloop()