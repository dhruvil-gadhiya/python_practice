# Given a list of words, group them into a dictionary where the key is word length and the value is a list of words of that length...

words = input("Enter words separated by spaces: ").split()

length_dict = {}

for word in words:
    length = len(word)
    if length not in length_dict:
        length_dict[length] = [word]
    else:
        length_dict[length].append(word)

print("\nWords grouped by their length:")
for length, group in length_dict.items():
    print(f"Length {length}: {group}")

