# Given a list with repeated elements, create a new list with only unique values...

original_list = [1, 2, 2, 3, 4, 4, 5, 1]

unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original list:", original_list)
print("List without duplicates:", unique_list)

