# Generate a random number between 1 and 10, then let the user guess it and give feedback on whether the guess is correct...

import random

score = 0
attempts = 0

while True:
    secret_number = random.randint(1,10)

    try:
        guess_number = int(input("Guess a number between 1 to 10: "))
        print("Attempts so far : ",attempts)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue  # Skip the rest and go back to the beginning

    print("Random number:", secret_number)

    if guess_number <= 0 and guess_number >= 10:
        print("PLEASE... enter a valid number...")
    elif secret_number == guess_number:
        print("Congratulation... YOU guess right number..!!!")
        score += 1
    else: 
        print("SORRY... you loss the game...!!!")
        # score -= 1

    print("Your current score is : ",score)

    again = input("\nDo you want another chance? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Your final score is : ",score)
        break

