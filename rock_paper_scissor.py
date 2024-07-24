# TODO: Task No 2: ROCK PAPER SCISSOR GAME
"""
Winning Rules as follows:
Rock vs paper -> paper wins
Rock vs scissor -> Rock wins
paper vs scissor -> scissor wins.
"""

import tkinter as tk
from tkinter import messagebox
import random

def RPSgame(UserChoice):
    ComputerChoice = random.choice(['rock', 'paper', 'scissor'])
    result = ""
    if UserChoice == ComputerChoice:
        result = "It's a tie!"
    elif (UserChoice == "rock" and ComputerChoice == "paper") or \
         (UserChoice == "paper" and ComputerChoice == "scissor") or \
         (UserChoice == "scissor" and ComputerChoice == "rock"):
        result = "You lose!"
    else:
        result = "You won!"
    result_label.config(text=f"Computer chose {ComputerChoice}\nYou chose {UserChoice}\n{result}")

def resetGame():
    result_label.config(text="")

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("300x250")
root.config(bg="AliceBlue")

tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 16), bg="AliceBlue").pack(pady=10)
result_label = tk.Label(root, font=("Helvetica", 14), bg="AliceBlue")
result_label.pack(pady=20)

buttonFrame = tk.Frame(root, bg="AliceBlue")
buttonFrame.pack(pady=10)

rockButton = tk.Button(buttonFrame, text="Rock", font=("Helvetica", 12), bg="LightCoral", command=lambda: RPSgame("rock"))
rockButton.pack(side=tk.LEFT, padx=5, pady=5)

paperButton = tk.Button(buttonFrame, text="Paper", font=("Helvetica", 12), bg="LightGreen", command=lambda: RPSgame("paper"))
paperButton.pack(side=tk.LEFT, padx=5, pady=5)

scissorButton = tk.Button(buttonFrame, text="Scissor", font=("Helvetica", 12), bg="LightSteelBlue", command=lambda: RPSgame("scissor"))
scissorButton.pack(side=tk.LEFT, padx=5, pady=5)

tk.Button(root, text="Reset", font=("Helvetica", 12), bg="PeachPuff", command=resetGame).pack(pady=10)

root.mainloop()
