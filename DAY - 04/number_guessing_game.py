# Generate a random number between 1 and 20. Let the user guess the number. Give hints like "Too high" or "Too low" until they guess it. Count the number of attempts...

import random

# Generate a random number between 1 and 20
secret_number = random.randint(1,20)

# Initialize attempt counter
attempts = 0

print("I'm thinking of a number between 1 and 20. Can you guess it?")

while True:
    guess = int(input("Enter your guess : "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
        break



