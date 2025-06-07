"""
CP1404 Practical
This programs converts temperatures from Celsius to Fahrenheit and vice versa.
"""

MENU = """ C - Convert from Celsius to Fahrenheit
 F - Convert from Fahrenheit to Celsius
 Q - Quit """

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")
    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")
    else:
        print("Invalid choice. Please try again.")
    print(MENU)
    choice = input(">>> ").upper()
print("Goodbye!")

