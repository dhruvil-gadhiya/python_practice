# Ask the user to input a positive number N. Find the sum of all numbers below N that are divisible by 3 or 5...

# Ask the user for input
N = int(input("Enter a positive number: "))

# Initialize a variable to store the sum
total = 0

# Loop through numbers from 1 to N-1
for i in range(1, N):
    if i % 3 == 0 or i % 5 == 0:
        total += i

# Print the result
print("Sum of multiples of 3 or 5 below", N, "is:", total)
