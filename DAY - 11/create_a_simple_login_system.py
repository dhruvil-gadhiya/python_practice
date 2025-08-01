# Store a predefined username and password, then ask the user to input credentials and validate them...

correct_username = "admin"
correct_password = "1234"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login successful! ✅")
else:
    print("Invalid username or password. ❌")


