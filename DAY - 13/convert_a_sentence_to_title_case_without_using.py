# Ask the user for a sentence and convert the first letter of each word to uppercase manually...

sentence = input("Enter a sentence: ")

words = sentence.split()

title_case_words = []
for word in words:
    if word:
        capitalized = word[0].upper() + word[1:]
        title_case_words.append(capitalized)

title_case_sentence = ' '.join(title_case_words)

print("Title case : ",title_case_sentence)

    