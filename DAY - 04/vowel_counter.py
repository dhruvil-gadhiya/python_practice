# Write a program that takes a string from the user and counts how many vowels (a, e, i, o, u) are in it. Ignore case sensitivity...

# Ask the user to enter a word or sentence
text = input("Enter a word or sentence: ")

# Convert the text to lowercase to make it case-insensitive
text = text.lower()

# Define the vowels
vowels = "aeiou"

# Initialize a counter
count = 0

# Loop through each character in the text
for char in text:
    if char in vowels:
        count += 1

# Print the result
print("Number of vowels:", count)



