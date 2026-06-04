import tkinter as tk
from tkinter import messagebox

# Scores
player_score = 0
computer_score = 0

# Counter moves to ensure computer wins
winning_move = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
}

def play(player_choice):
    global player_score, computer_score

    computer_choice = winning_move[player_choice]

    result = f"Player chose: {player_choice}\n"
    result += f"Computer chose: {computer_choice}\n\n"
    result += "Computer Wins!"

    computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"Player Score: {player_score}    Computer Score: {computer_score}"
    )

def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    result_label.config(text="Choose Rock, Paper, or Scissors")
    score_label.config(
        text=f"Player Score: {player_score}    Computer Score: {computer_score}"
    )

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors - Computer Always Wins")
root.geometry("600x450")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

instruction = tk.Label(
    root,
    text="Choose your move",
    font=("Arial", 12)
)
instruction.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(
    button_frame,
    text="Rock",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    button_frame,
    text="Paper",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

scissor_btn = tk.Button(
    button_frame,
    text="Scissors",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Scissors")
)
scissor_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 14),
    justify="center"
)
result_label.pack(pady=30)

score_label = tk.Label(
    root,
    text="Player Score: 0    Computer Score: 0",
    font=("Arial", 14, "bold")
)
score_label.pack(pady=10)

reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12),
    width=15,
    command=reset_game
)
reset_btn.pack(pady=20)

root.mainloop()