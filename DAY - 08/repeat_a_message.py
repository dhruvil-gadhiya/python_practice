# Ask the user for a message and a number, then print the message that many times...

message = input("Enter a messsage : ")

try:
    count = int(input("Enter a number for repeting the message : "))

    if count < 0:
        print("Please enter a non-negative number.")
    else:
        for i in range(count):
            print(f"{i + 1}. {message}")

except ValueError:
    print("Invalid input. Please enter a valid number.")


