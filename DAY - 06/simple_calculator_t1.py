# Allow the user to perform multiple operations (like +, -, *, /) in one run without restarting the program...

while True:
    print("\nWelcome to the Multi-Operation Calculator!")
    expression = input("Enter a math expression (e.g. 2 + 3 * 4 - 1): ")

    try:
        # Evaluate full expression
        result = eval(expression)
        print("Result:", result)

    except NameError:
        print("ERROR: Avoid using letters or undefined names. Use only numbers and math symbols.")

    except ZeroDivisionError:
        print("ERROR: You tried dividing by zero. That's not allowed.")

    except SyntaxError:
        print("ERROR: There's something wrong with your syntax. Check operators and numbers.")

    except Exception as e:
        print(f"ERROR: Unexpected issue occurred ({type(e).__name__}). Please try again.")

    # Ask if user wants to continue
    again = input("\nDo you want to enter another expression? (yes/no): ").strip().lower()
    if again != "yes":
        print("\nThanks for using the calculator. See you next time!")
        break
