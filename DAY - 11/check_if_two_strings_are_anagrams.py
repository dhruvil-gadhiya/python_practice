# Ask the user for two strings and check if they are anagrams (contain the same letters in different order)...

str1 = input("Enter the first string: ").lower().replace(" ", "")
str2 = input("Enter the second string: ").lower().replace(" ", "")


if sorted(str1) == sorted(str2):
    print("The strings are anagrams!")
else:
    print("The strings are NOT anagrams.")





