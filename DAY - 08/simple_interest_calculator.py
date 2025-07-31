# Ask the user for principal, rate, and time, then calculate and display the simple interest...

principal = float(input("Enter a principle : "))

rate = float(input("Enter a rate of interest : "))

time = float(input("Enter a period of time : "))


Simple_Interest = principal * rate * time / 100

print("Simple Interest is : ", Simple_Interest)

