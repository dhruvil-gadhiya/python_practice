# Ask the user for a number n and generate a list of squares from 1 to n using list comprehension...

n = int(input("Enter a number: "))

squares = [i**2 for i in range(1, n + 1)]

print("List of squares from 1 to", n, ":", squares)

