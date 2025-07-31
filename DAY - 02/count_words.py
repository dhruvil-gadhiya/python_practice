# Count Words in a Sentence...

# Ask the user to enter a sentence and store it in the variable 'user_input'
user_input = input("Enter the sentence : ")

word = user_input.split()                                 # Use .split() to break the sentence into words based on spaces (handles multiple spaces automatically)
print(word)                                               # Print the list of words (for verification/debugging)

count = len(word)                                         # Count the number of words by measuring the length of the list
print(count)                                              # Print the total word count

