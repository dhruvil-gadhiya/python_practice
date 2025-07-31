# Print Even Numbers in a Range...

# Ask the user for the start and end numbers
start_input = int(input("Enter the start number: "))
end_input = int(input("Enter the end number: "))

# Adjust start number if it's odd (so we start with an even number)
if start_input % 2 != 0:
    start_input += 1  # Move to the next even number

# Use range with step 2 to print even numbers
for count in range(start_input, end_input + 1, 2):
    print(count)

