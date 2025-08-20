# Given a Python algorithm (like a nested loop or search function), analyze its time complexity (Big O) and space complexity...

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):          # loop runs n times
        if arr[i] == target:
            return i
    return -1

# Binary Search (iterative)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:                 # loop runs log n times
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
nums = [2, 4, 6, 8, 10, 12, 14, 16]

print("Linear Search (target=10):", linear_search(nums, 10))
print("Binary Search (target=10):", binary_search(nums, 10))


