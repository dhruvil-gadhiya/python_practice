# Ask the user for a sentence and return it with all punctuation marks removed...

import string

text = input("Enter a sentence: ")

translator = str.maketrans('', '', string.punctuation)

cleaned_text = text.translate(translator)

print("Text without punctuation:", cleaned_text)

