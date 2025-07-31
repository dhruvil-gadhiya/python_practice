# Ask the user for a word and count how many vowels it contains...

text = input("Enter a sentence : ")

text = text.lower()

vowels = "aeiou"

count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)


