# Project Title: Rock-Paper-Scissors Game...
# Question: Create a program where the user plays Rock, Paper, Scissors against the computer. The computer randomly chooses one of the three options, and the winner is decided based on the classic rules. Include a score tracker and the option to play again...

import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid input. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock Paper Scissors ---")
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        winner = decide_winner(user, computer)

        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()


