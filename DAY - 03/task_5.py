# Python Program to Solve Quadratic Equation...

import cmath  # Use cmath to handle complex solutions as well

# Get coefficients a, b, and c from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = (b**2) - (4 * a * c)

# Find two solutions using the quadratic formula
root1 = (-b + cmath.sqrt(d)) / (2 * a)
root2 = (-b - cmath.sqrt(d)) / (2 * a)

# Display the results
print("\nThe solutions to the equation are:")
print("x1 =", root1)
print("x2 =", root2)

