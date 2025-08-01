# Determine whether the input sentence contains every letter of the alphabet at least once...

import string

sentence = input("Enter a sentence: ").lower()

alphabet_set = set(string.ascii_lowercase)

sentence_set = set(char for char in sentence if char.isalpha())

if alphabet_set.issubset(sentence_set):
    print("The sentence is a Pangram.")
else:
    print("The sentence is NOT a Pangram.")

