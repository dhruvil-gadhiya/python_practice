# Ask the user for a number and calculate its factorial...

number = int(input("Enter a number: "))

# Case 1: Negative number
if number < 0:
    print("PLEASE... enter a POSITIVE NUMBER. Factorial is not defined for negative numbers.")

# Case 2: Zero (special case)
elif number == 0:
    print("0! = 1")

# Case 3: Positive number
else:
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    print(f"FACTORIAL of {number} is {fact}")




