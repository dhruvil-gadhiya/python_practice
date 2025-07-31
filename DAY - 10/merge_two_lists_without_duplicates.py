# Combine two lists into one new list that contains only unique elements...

User_input_1 = input("Enter a number for list like this way (e.g : 10, 20, 30, 40, 50) :  ")
string_list = User_input_1.split(",")
l1 = [int(num.strip()) for num in string_list]


User_input_2 = input("Enter a number for list like this way (e.g : 10, 20, 30, 40, 50) :  ")
string_list = User_input_2.split(",")
l2 = [int(num.strip()) for num in string_list]

print("Your list of l1 : ", l1)
print("Your list of l2 : ", l2)


combined = l1 + l2

unique = list(set(combined))

print("unique list : ",unique)
