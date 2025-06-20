"""
CP1404/CP5632 - Practical

Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"Questions:"
# 1. When will a ValueError occur?
# When the user enters a non-numeric value for the numerator or denominator such as "a" or "1 2".

# 2. When will a ZeroDivisionError occur?
# When the user enters a denominator of 0.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, we can change the code to avoid the possibility of a ZeroDivisionError by adding a try-except block around the division operation.
