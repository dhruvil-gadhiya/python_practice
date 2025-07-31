# Calculate Compound Interest...

# Ask the user to input principal, rate, and time
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Annual Interest Rate (in %): "))
T = float(input("Enter the Time (in years): "))

A = P * (1 + R / 100) ** T                                   # Calculate the total amount after interest

CI = A - P                                                   # Calculate compound interest earned

# Display the result
print("Total Amount (A):", round(A, 2))
print("Compound Interest (CI):", round(CI, 2))

