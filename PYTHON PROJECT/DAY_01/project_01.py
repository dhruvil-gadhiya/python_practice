# Project Title: Calculator...
# Question: Build a simple command-line calculator that can perform basic operations: addition, subtraction, multiplication, and division. The user should be able to input two numbers and choose an operation. Handle division by zero gracefully...


while True:
    # Ask the user for two numbers first
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    # Show operation menu
    print("\nSelect the operation:")
    print("1: ADD (+)")
    print("2: SUB (-)")
    print("3: MUL (*)")
    print("4: DIV (/)")

    # Get user choice
    choice = int(input("Enter your choice (1-4): "))


    # Perform the chosen operation
    if choice == 1:
        result = num1 + num2
        print("SUM of num1 & num2 is:", result)

    elif choice == 2:
        result = num1 - num2
        print("SUBTRACTION of num1 & num2 is:", result)

    elif choice == 3:
        result = num1 * num2
        print("MULTIPLICATION of num1 & num2 is:", result)

    elif choice == 4:
        if num2 == 0:
            print("You entered ZERO, which is NOT divisible...")
        else:
            result = num1 / num2
            print("DIVISION of num1 & num2 is:", result)

    else:
        print("PLEASE enter a valid choice (1 to 4).")

    # Ask the user if they want to continue
    again = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for using the calculator. Goodbye!")
        break




