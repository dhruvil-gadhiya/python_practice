# Ask the user for a word and check if it reads the same forward and backward...

User_input = input("Enter a word : ")

rev_input = User_input[::-1]

print(rev_input)

if User_input == rev_input:
    print("This word is PALINDROME...")
else:
    print("This word is NOT PALINDROME...")

