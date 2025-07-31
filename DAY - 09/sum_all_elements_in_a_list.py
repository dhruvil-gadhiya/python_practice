#  Create a list of numbers and calculate the total sum using a loop or built-in function...

User_input = input("Enter a number for list like this way (e.g : 10, 20, 30, 40, 50) :  ")

string_list = User_input.split(",")

numbers = [int(num.strip()) for num in string_list]

print("Your list of numbers : ", numbers)



sum = sum(numbers)

print("SUM OF LIST IS : ",sum)

