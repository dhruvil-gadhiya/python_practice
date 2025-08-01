# Given a list of elements, create a dictionary where keys are unique elements and values are their frequencies...

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'mango']

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency dictionary:", frequency)



