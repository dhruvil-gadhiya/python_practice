# Given a list like [1, [2, 3], 4, [5, 6]], convert it to [1, 2, 3, 4, 5, 6]. ...


nested_list = [1, [2, 3], 4, [5, 6]]

flattened_list = []

for item in nested_list:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print("Flattened list:", flattened_list)

