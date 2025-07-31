# Ask the user for their age and print a message like "You are an adult" if the age is 18 or more...

age = int(input("Enter your age : "))

if age < 0 :
    print("You entered negative age... PLEASE enter valid age...")
elif age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

