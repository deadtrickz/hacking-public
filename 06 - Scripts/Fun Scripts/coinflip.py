#!/bin/python3
import random

class Scoreboard:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def update_score(self, winner):
        if winner == 'player':
            self.player_score += 1
        elif winner == 'computer':
            self.computer_score += 1

def play_game(scoreboard):
    choices = ['heads', 'tails']
    result = random.choice(choices)
    choice = input("Enter heads or tails: ")
    if choice in ['heads', 'h'] and result in ['tails', 't']:
        print("You lose!")
        scoreboard.update_score('computer')
    elif choice in ['tails', 't'] and result in ['heads', 'h']:
        print("You lose!")
        scoreboard.update_score('computer')
    else:
        print("You win!")
        scoreboard.update_score('player')
    print(f"Player score: {scoreboard.player_score}, Computer score: {scoreboard.computer_score}")

scoreboard = Scoreboard()
while True:
    play_game(scoreboard)
    again = 'n'
    if again == 'y':
        break
print("Thanks for playing!")
