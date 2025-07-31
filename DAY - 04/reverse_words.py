# Take a sentence input from the user and reverse the order of the words, but not the words themselves... Example: "Hello world from Python" → "Python from world Hello"...

user_input = input("Enter a sentence: ")                        # Step 1: Take input from the user

words = user_input.split()                                      # Step 2: Split the sentence into a list of words

reversed_words = words[::-1]                                    # Step 3: Reverse the list of words

reversed_sentence = " ".join(reversed_words)                    # Step 4: Join the reversed words back into a sentence

print("Reversed sentence:", reversed_sentence)                  # Step 5: Display the result

