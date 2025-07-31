# Ask the user for a string input. Then, display how many times each character appears in the string (excluding spaces)...

text = input("Enter a string : ")                    # Ask the user for input

text = text.replace(" ","")                          # Remove spaces from the text

char_count = {}                                      # Create an empty dictionary to hold character counts

# Loop through each character in the string
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Display the frequency of each character
print("Character frequencies:")
for char, count in char_count.items():
    print(f"{char} : {count}")

