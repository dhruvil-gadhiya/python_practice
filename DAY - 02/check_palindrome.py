# Check Palindrome...

user_input = input("Enter a word or number: ")               # Ask the user to enter a word or number

reversed_input = user_input[::-1]                            # Reverse the input using slicing


if user_input == reversed_input:                             # Check if the original and reversed are the same
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
