# Given a list of numbers, find and display the second largest value...

# Sample list of numbers
numbers = [10, 40, 30, 20, 50, 50]

# Remove duplicates to avoid repeated largest numbers
unique_numbers = list(set(numbers))

# Check if there are at least two unique values
if len(unique_numbers) < 2:
    print("There is no second largest number (list has less than 2 unique values).")
else:
    # Sort the list in descending order
    unique_numbers.sort(reverse=True)

    # The second element is the second largest
    print("The second largest number is:", unique_numbers[1])

