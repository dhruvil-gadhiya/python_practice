# Ask the user to enter a list of numbers and determine if the list is sorted in ascending order...

# Ask the user to enter numbers separated by spaces
user_input = input("Enter a list of numbers separated by space: ")

# Convert the input string into a list of integers
user_list = list(map(int, user_input.split()))

# Check if the list is sorted in ascending order
if user_list == sorted(user_list):
    print("The list is sorted in ascending order.")
else:
    print("The list is NOT sorted in ascending order.")


