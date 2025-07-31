# Python Program to Generate a Random Number...

import random  # Import the 'random' module to generate random numbers

# Ask the user to enter the upper limit for random number generation
N = int(input("Enter the ending number for random choice : "))

# Generate and print a random integer between 0 and N (inclusive)
print(random.randint(0, N))
