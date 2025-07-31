# Ask the user how many numbers they want to enter, take the inputs, and calculate the average...

# Ask how many numbers the user wants to enter
count = int(input("How many numbers do you want to enter? "))

# Initialize a total sum variable
total = 0

# Loop to take N inputs and calculate the sum
for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    total += num

# Calculate average
average = total / count

# Print the result
print(f"The average of the {count} numbers is: {average}")

