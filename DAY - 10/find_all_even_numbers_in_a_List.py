# Given a list of integers, extract and print only the even numbers...

User_input = input("Enter a number for list like this way (e.g : 10, 20, 30, 40, 50) :  ")

string_list = User_input.split(",")

numbers = [int(num.strip()) for num in string_list]

print("Your list of numbers : ", numbers)

even_number = []

for i in numbers:
    if i % 2 == 0:
        print(f"{i} is an EVEN NUMBER...")
        even_number.append(i)

print("\nList of even numbers:", even_number)



