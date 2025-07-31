# Given a list, determine which element appears the most times...


elements = [1, 3, 2, 1, 4, 1, 3, 2, 3, 3]

frequency = {}

for item in elements:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

most_frequent = max(frequency, key=frequency.get)

print(f"The most frequent element is: {most_frequent}")
print(f"It appears {frequency[most_frequent]} times.")

