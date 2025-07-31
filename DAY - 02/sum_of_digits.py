# Sum of All Digits in a Number...


num = int(input("Enter the number : "))                                 # Ask the user to enter a number and convert it to an integer

sum = 0                                                                 # Initialize a variable to hold the sum of digits

for i in str(num):                                                      # Convert the number to a string to loop through each digit
    sum += int(i)                                                       # Convert each character back to integer and add it to the sum

print(sum)                                                              # Print the final result (sum of all digits)
