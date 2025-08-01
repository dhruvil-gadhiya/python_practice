# Project Title: Word Counter...
# Question: Ask the user to input a sentence or a paragraph, then count and display:...

from collections import Counter

text = input("Enter a sentence or paragraph: ")

words = text.split()

total_words = len(words)

total_characters = len(text.replace(" ", ""))

word_counts = Counter(word.lower() for word in words)

most_common_word, freq = word_counts.most_common(1)[0]

print("\n--- Word Count Summary ---")
print(f"Total words: {total_words}")
print(f"Total characters (excluding spaces): {total_characters}")
print(f"Most common word: '{most_common_word}' (appeared {freq} times)")

