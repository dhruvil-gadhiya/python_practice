# Check if a Number is a Multiple of Another...

# Ask the user to input the first number (a)
num_1 = int(input("Enter the value for 'a' : "))

# Ask the user to input the second number (b)
num_2 = int(input("Enter the value for 'b' : "))

# Calculate the square of num_1 (this is not needed for checking multiples)
mul = num_1 * num_1
print(mul)  # Print the square of num_1 (for reference or debugging)

# Check if num_2 is equal to the square of num_1
# (⚠️ This does not check for multiples. Correct logic is in the commented line below)
if mul == num_2:
# if num_2 % num_1 == 0:  # ✅ Correct logic to check if b is a multiple of a
    print(num_2, "is multiple of", num_1)
else:
    print(num_2, "is NOT a multiple of", num_1)
