# Project Title: Even or Odd Checker...
# Question: Ask the user to enter a number. Tell them if the number is even or odd. Then ask if they want to try again...

while True:
    try:
        user_input = int(input("Enter a number: "))

        if user_input % 2 == 0:
            print(f"{user_input} is an EVEN number.")
        else:
            print(f"{user_input} is an ODD number.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    check_again = input("Do you want to check another number? (yes/no): ").lower()
    if check_again != "yes":
        print("Thanks for using Even/Odd Checker!")
        break

