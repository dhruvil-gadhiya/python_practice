# Ask the user for a list and a specific value, then print the index of that value in the list (if it exists)...

user_input = input("Enter items separated by space: ")
my_list = user_input.split()


value = input("Enter the value to search for: ")


if value in my_list:
    print(f"'{value}' is found in the list at index {my_list.index(value)}.")
else:
    print(f"'{value}' is NOT found in the list.")

index = my_list.index(value)
print(f"'{value}' found at index {index}")

