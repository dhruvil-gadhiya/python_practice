# Ask the user for a single letter and tell whether it’s a vowel or a consonant...

letter = input("Enter a single letter : ")

letter = letter.lower()
print(letter)

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Enter letter is vowels...")
else:
    print("Enter number is consonant...")






# # chatGPT code :

# # Ask the user to enter a single character
# char = input("Enter a single letter: ").lower()

# # Check if input is a single alphabet letter
# if len(char) == 1 and char.isalpha():
#     if char in "aeiou":
#         print(f"'{char}' is a vowel.")
#     else:
#         print(f"'{char}' is a consonant.")
# else:
#     print("Invalid input. Please enter a single alphabet letter.")
