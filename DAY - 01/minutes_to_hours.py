# Convert Minutes to Hours and Minutes (Formatted and Commented)
import math

# Step 1: Get input from the user
Minutes = int(input("Enter the total minutes: "))

# Step 2: Convert total minutes to decimal hours
hours = Minutes / 60
print("Decimal hours:", hours)

# Step 3: Get the whole number of hours
converted = int(hours)
print("Whole hours:", converted)

# Step 4: Get the fractional part using math.modf (returns fractional, then integer part)
fraction, whole = math.modf(hours)
print("Fractional part (in hours):", fraction)

# Step 5: Convert fractional hours to minutes
m = fraction * 60
print("Fractional part as minutes:", m)

# Step 6: Round the minutes to nearest whole number
r = round(m)
print("Rounded minutes:", r)

# Step 7: Final formatted output
print("\n--- Formatted Output ---")
print(f"{Minutes} minutes is equal to {converted} hour(s) and {r} minute(s).")










# ---- This is other Method.........


# # Ask the user to enter total minutes
# total_minutes = int(input("Enter total minutes: "))

# # Calculate hours and remaining minutes
# hours = total_minutes // 60
# minutes = total_minutes % 60

# # Display the result
# print(f"{total_minutes} minutes is {hours} hour(s) and {minutes} minute(s).") 