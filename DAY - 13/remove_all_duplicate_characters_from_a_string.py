# Take a string as input and return a version with only the first occurrence of each character (maintaining order)...

input_str = input("Enter a string: ")

result = ""
seen = set()

for char in input_str:
    if char not in seen:
        seen.add(char)
        result += char

print("String without duplicates:", result)
