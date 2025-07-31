# Take a number as input and count how many digits it has...

# Ask the user to enter a number
user_input = input("Enter a number: ")

# Remove negative sign if present
if user_input.startswith('-'):
    user_input = user_input[1:]

# Check if input is a valid number
if user_input.isdigit():
    digit_count = len(user_input)
    print(f"The number has {digit_count} digits.")
else:
    print("Invalid input. Please enter a valid integer number.")


