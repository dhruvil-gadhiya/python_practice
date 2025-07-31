# Ask the user to input an email and check if it contains @, a domain, and no spaces...

email = input("Enter your email address: ")


if "@" in email and "." in email and " " not in email:
    at_index = email.index("@")
    dot_index = email.rfind(".")

    if 0 < at_index < dot_index < len(email) - 1:
        print("Valid email address.")
    else:
        print("Invalid email: Incorrect position of '@' or '.'")
else:
    print("Invalid email: Must contain '@', domain, and no spaces.")

