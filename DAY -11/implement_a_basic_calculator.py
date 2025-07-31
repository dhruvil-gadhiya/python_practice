# Ask the user for two numbers and an operator (+, -, *, /), then perform the corresponding operation...

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print(f"The result is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"The result is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"The result is: {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator. Please choose +, -, *, or /.")

