# Write a program to sort a list of numbers manually (e.g., using bubble sort or any basic algorithm)...

# numbers = [25, 115, 98, 1, 45, 30]

User_input_1 = input("Enter a number for list like this way (e.g : 10, 20, 30, 40, 50) :  ")
string_list = User_input_1.split(",")
numbers = [int(num.strip()) for num in string_list]

n = len(numbers)

for i in range(n):
    for j in range(0,  n-i-1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:",numbers)

