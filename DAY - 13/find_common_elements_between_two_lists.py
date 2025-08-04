# Take two lists from the user and print the elements that appear in both...

User_input1 = input("Enter a number for list like this way (e.g : 10, 20, 30, 40, 50) :  ")
string_list = User_input1.split(",")
l1 = [int(num.strip()) for num in string_list]

User_input2 = input("Enter a number for list like this way (e.g : 10, 20, 30, 40, 50) :  ")
string_list = User_input2.split(",")
l2 = [int(num.strip()) for num in string_list]

l3 = []


# for i in range(len(l1)):
#     for j in range(len(l2)):
#         if l1[i] == l2[j]:
#             l3.append(l1[i])

# print("Common elements:", l3)
        

for item in l1:
    if item in l2:
        l3.append(item)

print("Common elements:", l3)      


