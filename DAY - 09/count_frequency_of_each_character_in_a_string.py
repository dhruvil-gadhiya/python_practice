# Ask the user for a string and count how many times each character appears...

text = input("Enter a string: ")
text = text.lower()

char_freq = {}

for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("\nCharacter Frequency:")

for char, count in char_freq.items():
    print(f"'{char}' : {count}")

