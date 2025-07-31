# Repeat a Message Multiple Times...

# Ask the user for a message
message = input("Enter a message: ")

# Ask how many times to repeat it
count = int(input("How many times should I repeat it? "))

# Print the message that many times
for i in range(count):
    print(message)
