# Python Program to Check Prime Number...

number = int(input("Enter the number: "))

if number < 2:
    print(f"{number} is NOT a PRIME NUMBER.")
else:
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print(f"{number} is a PRIME NUMBER.")
    else:
        print(f"{number} is NOT a PRIME NUMBER.")
